class ProdutoController:
    def __init__(self, db_operations):
        self.db_operations = db_operations

    def adicionar_produto(self, nome, descricao, preco, quantidade):
        if quantidade < 0 or preco < 0:
            raise ValueError("Preço e quantidade devem ser valores não negativos.")
        produto_id = self.db_operations.adicionar_produto(nome, descricao, preco, quantidade)
        return produto_id

    def atualizar_produto(self, produto_id, nome, descricao, preco, quantidade):
        if quantidade < 0 or preco < 0:
            raise ValueError("Preço e quantidade devem ser valores não negativos.")
        self.db_operations.atualizar_produto(produto_id, nome, descricao, preco, quantidade)

    def remover_produto(self, produto_id):
        self.db_operations.remover_produto(produto_id)

    def listar_produtos(self):
        return self.db_operations.listar_produtos()

    def buscar_produto(self, produto_id):
        return self.db_operations.buscar_produto(produto_id)