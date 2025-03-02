from tkinter import Tk
from views.tela_principal import TelaPrincipal

def main():
    root = Tk()
    root.title("Sistema de Estoque")
    root.geometry("800x600")  # Definindo o tamanho da janela
    root.resizable(False, False)  # Impedindo redimensionamento da janela

    app = TelaPrincipal(root)
    app.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()