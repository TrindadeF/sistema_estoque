def conectar():
    import mysql.connector
    from mysql.connector import Error
    from configparser import ConfigParser

    config = ConfigParser()
    config.read('config.ini')

    try:
        conexao = mysql.connector.connect(
            host=config['mysql']['host'],
            user=config['mysql']['user'],
            password=config['mysql']['password'],
            database=config['mysql']['database']
        )
        if conexao.is_connected():
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None


def adicionar_produto(nome, descricao, preco, quantidade):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "INSERT INTO produtos (nome, descricao, preco, quantidade) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nome, descricao, preco, quantidade))
        conexao.commit()
        cursor.close()
        conexao.close()


def remover_produto(produto_id):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "DELETE FROM produtos WHERE id = %s"
        cursor.execute(sql, (produto_id,))
        conexao.commit()
        cursor.close()
        conexao.close()


def atualizar_produto(produto_id, nome, descricao, preco, quantidade):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "UPDATE produtos SET nome = %s, descricao = %s, preco = %s, quantidade = %s WHERE id = %s"
        cursor.execute(sql, (nome, descricao, preco, quantidade, produto_id))
        conexao.commit()
        cursor.close()
        conexao.close()


def listar_produtos():
    conexao = conectar()
    produtos = []
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        cursor.close()
        conexao.close()
    return produtos


def registrar_movimentacao(produto_id, tipo, quantidade):
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "INSERT INTO movimentacoes (produto_id, tipo, data_hora, quantidade) VALUES (%s, %s, NOW(), %s)"
        cursor.execute(sql, (produto_id, tipo, quantidade))
        conexao.commit()
        cursor.close()
        conexao.close()


def listar_movimentacoes():
    conexao = conectar()
    movimentacoes = []
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM movimentacoes")
        movimentacoes = cursor.fetchall()
        cursor.close()
        conexao.close()
    return movimentacoes