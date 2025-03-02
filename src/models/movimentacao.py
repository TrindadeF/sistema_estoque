class Movimentacao:
    def __init__(self, produto_id, tipo, data_hora, quantidade):
        self.produto_id = produto_id
        self.tipo = tipo  # 'inclusão' ou 'retirada'
        self.data_hora = data_hora
        self.quantidade = quantidade

    def __repr__(self):
        return f"Movimentacao(produto_id={self.produto_id}, tipo='{self.tipo}', data_hora='{self.data_hora}', quantidade={self.quantidade})"