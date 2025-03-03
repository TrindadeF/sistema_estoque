import mysql.connector
import configparser

class ProdutoRepository:
    def __init__(self):
        self.config = self._load_config()
    
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
    
    def listar_todos(self):
        """Retorna todos os produtos"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT p.id, p.nome, p.descricao, p.preco, p.quantidade, p.categoria_id, c.nome
        FROM produtos p
        LEFT JOIN categorias c ON p.categoria_id = c.id
        ''')
        
        produtos = []
        for row in cursor.fetchall():
            produtos.append({
                'id': row[0],
                'nome': row[1],
                'descricao': row[2],
                'preco': row[3],
                'quantidade': row[4],
                'categoria_id': row[5],
                'categoria_nome': row[6]
            })
        
        conn.close()
        return produtos
    
    def obter_por_id(self, produto_id):
        """Retorna um produto pelo ID"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT p.id, p.nome, p.descricao, p.preco, p.quantidade, p.categoria_id, c.nome
        FROM produtos p
        LEFT JOIN categorias c ON p.categoria_id = c.id
        WHERE p.id = %s
        ''', (produto_id,))
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {
                'id': row[0],
                'nome': row[1],
                'descricao': row[2],
                'preco': row[3],
                'quantidade': row[4],
                'categoria_id': row[5],
                'categoria_nome': row[6]
            }
        return None
    
    def obter_id_por_nome(self, nome_produto):
        """Retorna o ID do produto pelo nome"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT id FROM produtos WHERE nome = %s', (nome_produto,))
        row = cursor.fetchone()
        conn.close()
        
        return row[0] if row else None