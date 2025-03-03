import mysql.connector
import configparser
from datetime import datetime

class MovimentacaoRepository:
    def __init__(self):
        self.config = self._load_config()
        self._init_db()
    
    def _load_config(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config
    
    def _get_connection(self):
        """Estabelece conexão com o banco de dados"""
        return mysql.connector.connect(
            host=self.config['database']['host'],
            user=self.config['database']['user'],
            password=self.config['database']['password'],
            database=self.config['database']['database']
        )
    
    def _init_db(self):
        """Inicializa as tabelas no banco de dados"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        # Criar tabela de movimentações se não existir
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS movimentacoes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            data_hora DATETIME NOT NULL,
            produto_id INT NOT NULL,
            tipo VARCHAR(10) NOT NULL,
            quantidade INT NOT NULL,
            usuario VARCHAR(50) NOT NULL,
            observacoes TEXT,
            FOREIGN KEY (produto_id) REFERENCES produtos(id)
        )
        ''')
        
        conn.commit()
        conn.close()
    
    def registrar_movimentacao(self, produto_id, tipo, quantidade, usuario, observacoes=""):
        """Registra uma nova movimentação no estoque"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        data_hora = datetime.now()
        
        try:
            # Inserir na tabela de movimentações
            cursor.execute('''
            INSERT INTO movimentacoes 
            (data_hora, produto_id, tipo, quantidade, usuario, observacoes)
            VALUES (%s, %s, %s, %s, %s, %s)
            ''', (data_hora, produto_id, tipo, quantidade, usuario, observacoes))
            
            # Atualizar estoque do produto
            if tipo == "Entrada":
                cursor.execute('''
                UPDATE produtos SET quantidade = quantidade + %s
                WHERE id = %s
                ''', (quantidade, produto_id))
            else:  # Saída
                # Verifica se há estoque suficiente
                cursor.execute('SELECT quantidade FROM produtos WHERE id = %s', (produto_id,))
                estoque_atual = cursor.fetchone()[0]
                
                if estoque_atual < quantidade:
                    conn.rollback()
                    conn.close()
                    return False, "Estoque insuficiente para esta operação"
                
                cursor.execute('''
                UPDATE produtos SET quantidade = quantidade - %s
                WHERE id = %s
                ''', (quantidade, produto_id))
            
            conn.commit()
            return True, "Movimentação registrada com sucesso"
            
        except Exception as e:
            conn.rollback()
            return False, f"Erro ao registrar movimentação: {str(e)}"
            
        finally:
            conn.close()
    
    def listar_movimentacoes(self, limite=100):
        """Retorna as últimas movimentações registradas"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT m.id, m.data_hora, p.nome, m.tipo, m.quantidade, m.usuario, m.observacoes
        FROM movimentacoes m
        JOIN produtos p ON m.produto_id = p.id
        ORDER BY m.data_hora DESC
        LIMIT %s
        ''', (limite,))
        
        movimentacoes = []
        for row in cursor.fetchall():
            movimentacoes.append({
                'id': row[0],
                'data_hora': row[1],
                'produto': row[2],
                'tipo': row[3],
                'quantidade': row[4],
                'usuario': row[5],
                'observacoes': row[6]
            })
        
        conn.close()
        return movimentacoes