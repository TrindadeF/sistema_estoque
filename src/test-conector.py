import mysql.connector
from mysql.connector import Error

def testar_conexao():
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin123',
            database='estoque_sistema'
        )
        
        if conexao.is_connected():
            info_db = conexao.get_server_info()
            print(f"Conectado ao MySQL versão: {info_db}")
            
            cursor = conexao.cursor()
            cursor.execute("select database();")
            db = cursor.fetchone()
            print(f"Banco de dados: {db[0]}")
            
            cursor.close()
            conexao.close()
            print("Conexão encerrada")
            return True
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return False

if __name__ == "__main__":
    print("Testando conexão com o banco de dados...")
    testar_conexao()