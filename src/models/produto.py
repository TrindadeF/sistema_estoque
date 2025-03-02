class Produto:
    def __init__(self, nome, descricao, preco, quantidade):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade

    def remover_estoque(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
        else:
            raise ValueError("Quantidade a ser retirada é maior que a quantidade em estoque.")

    def __str__(self):
        return f"Produto(nome={self.nome}, descricao={self.descricao}, preco={self.preco}, quantidade={self.quantidade})"