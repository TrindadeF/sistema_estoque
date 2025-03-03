from tkinter import Tk
from views.tela_principal import TelaPrincipal
from database.init_db import inicializar_banco

def main():
    # Inicializa o banco de dados
    inicializar_banco()
    
    root = Tk()
    root.title("Sistema de Estoque")
    root.geometry("800x600")  # Definindo o tamanho da janela
    root.resizable(True, True)  # Permitindo redimensionamento da janela

    app = TelaPrincipal(root)
    app.pack(fill="both", expand=True)

    root.mainloop()

if __name__ == "__main__":
    main()