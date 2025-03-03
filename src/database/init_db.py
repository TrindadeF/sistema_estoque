import mysql.connector
import configparser
import os

def inicializar_banco():
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    try:
        # Conectar ao MySQL (sem especificar o banco)
        conn = mysql.connector.connect(
            host=config['database']['host'],
            user=config['database']['user'],
            password=config['database']['password']
        )
        
        cursor = conn.cursor()
        
        # Criar o banco de dados se não existir
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {config['database']['database']}")
        cursor.execute(f"USE {config['database']['database']}")
        
        # Criar tabelas
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS categorias (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) UNIQUE NOT NULL
        )
        ''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            descricao TEXT,
            preco DECIMAL(10,2) NOT NULL,
            quantidade INT NOT NULL DEFAULT 0,
            categoria_id INT,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id)
        )
        ''')
        
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
        
        # Inserir algumas categorias padrão se não existirem
        cursor.execute("SELECT COUNT(*) FROM categorias")
        if cursor.fetchone()[0] == 0:
            categorias = ["Eletrônicos", "Alimentos", "Vestuário", "Limpeza", "Ferramentas"]
            for categoria in categorias:
                cursor.execute("INSERT INTO categorias (nome) VALUES (%s)", (categoria,))
        
        conn.commit()
        print("Banco de dados inicializado com sucesso!")
        
    except mysql.connector.Error as err:
        print(f"Erro ao inicializar banco de dados: {err}")
        
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    inicializar_banco()