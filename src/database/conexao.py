import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

def criar_conexao():
    conexao = None
    try:
        conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password= os.getenv("DB_PASSWORD") | "",
            database='Almo_Rael'
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