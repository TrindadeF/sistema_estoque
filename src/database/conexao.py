import mysql.connector
from mysql.connector import Error

def criar_conexao():
    conexao = None
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='seu_usuario',
            password='sua_senha',
            database='nome_do_banco'
        )
        if conexao.is_connected():
            print("Conexão com o banco de dados estabelecida com sucesso.")
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
    return conexao

def fechar_conexao(conexao):
    """Fecha a conexão com o banco de dados."""
    if conexao.is_connected():
        conexao.close()
        print("Conexão com o banco de dados fechada.")