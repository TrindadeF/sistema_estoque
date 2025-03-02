class MovimentacaoController:
    def __init__(self, db_operations):
        self.db_operations = db_operations

    def registrar_inclusao(self, produto_id, quantidade):
        data_hora = self._obter_data_hora_atual()
        self.db_operations.adicionar_movimentacao(produto_id, 'inclusão', data_hora, quantidade)

    def registrar_retirada(self, produto_id, quantidade):
        data_hora = self._obter_data_hora_atual()
        self.db_operations.adicionar_movimentacao(produto_id, 'retirada', data_hora, quantidade)

    def _obter_data_hora_atual(self):
        from datetime import datetime
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')