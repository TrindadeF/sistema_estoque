# theme.py

class Theme:
    def __init__(self):
        self.bg_color = "#f0f0f0"  # Cor de fundo
        self.fg_color = "#333333"  # Cor do texto
        self.button_color = "#4CAF50"  # Cor dos botões
        self.button_hover_color = "#45a049"  # Cor do botão ao passar o mouse
        self.entry_color = "#ffffff"  # Cor dos campos de entrada
        self.font_family = "Arial"  # Fonte padrão
        self.font_size = 12  # Tamanho da fonte
        self.title_font_size = 16  # Tamanho da fonte do título

    def apply_theme(self, widget):
        widget.configure(bg=self.bg_color, fg=self.fg_color, font=(self.font_family, self.font_size))