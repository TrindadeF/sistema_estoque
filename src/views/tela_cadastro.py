import tkinter as tk
from tkinter import ttk, messagebox

class TelaCadastro(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        
        # Título da tela
        tk.Label(self, text="Cadastro de Produtos", font=("Helvetica", 16, "bold")).pack(pady=10)
        
        # Frame para o formulário
        form_frame = tk.LabelFrame(self, text="Dados do Produto", padx=20, pady=10)
        form_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Campos do formulário
        tk.Label(form_frame, text="Nome do Produto:").grid(row=0, column=0, sticky="w", pady=5)
        self.nome_entry = tk.Entry(form_frame, width=40)
        self.nome_entry.grid(row=0, column=1, sticky="w", pady=5)
        
        tk.Label(form_frame, text="Descrição:").grid(row=1, column=0, sticky="w", pady=5)
        self.descricao_text = tk.Text(form_frame, width=40, height=3)
        self.descricao_text.grid(row=1, column=1, sticky="w", pady=5)
        
        tk.Label(form_frame, text="Preço por Unidade (R$):").grid(row=2, column=0, sticky="w", pady=5)
        self.preco_entry = tk.Entry(form_frame, width=40)
        self.preco_entry.grid(row=2, column=1, sticky="w", pady=5)
        
        tk.Label(form_frame, text="Quantidade Inicial:").grid(row=3, column=0, sticky="w", pady=5)
        self.qtd_entry = tk.Entry(form_frame, width=40)
        self.qtd_entry.grid(row=3, column=1, sticky="w", pady=5)
        
        # Botões
        btn_frame = tk.Frame(self)
        btn_frame.pack(pady=10)
        
        self.btn_salvar = tk.Button(btn_frame, text="Salvar", command=self.salvar, width=15,
                                  bg="#4caf50", fg="white")
        self.btn_salvar.pack(side="left", padx=5)
        
        self.btn_limpar = tk.Button(btn_frame, text="Limpar", command=self.limpar_campos, width=15)
        self.btn_limpar.pack(side="left", padx=5)
        
        # Lista de produtos
        self.criar_lista_produtos()
    
    def criar_lista_produtos(self):
        lista_frame = tk.LabelFrame(self, text="Produtos Cadastrados", padx=20, pady=10)
        lista_frame.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Treeview para listar os produtos
        colunas = ("ID", "Nome", "Preço", "Quantidade")
        self.tabela = ttk.Treeview(lista_frame, columns=colunas, show="headings")
        
        # Definir cabeçalhos da tabela
        for col in colunas:
            self.tabela.heading(col, text=col)
            self.tabela.column(col, width=100, anchor="center")
        
        # Scrollbar para a tabela
        scrollbar = ttk.Scrollbar(lista_frame, orient="vertical", command=self.tabela.yview)
        self.tabela.configure(yscrollcommand=scrollbar.set)
        
        # Posicionar tabela e scrollbar
        self.tabela.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Botões de ação para a tabela
        btn_frame = tk.Frame(lista_frame)
        btn_frame.pack(fill="x", pady=5)
        
        self.btn_editar = tk.Button(btn_frame, text="Editar", command=self.editar_produto, width=15)
        self.btn_editar.pack(side="left", padx=5)
        
        self.btn_excluir = tk.Button(btn_frame, text="Excluir", command=self.excluir_produto, 
                                   width=15, bg="#f44336", fg="white")
        self.btn_excluir.pack(side="left", padx=5)
        
        # Adicionar dados de exemplo
        # Deverá ser substituído por dados do banco
        for i in range(5):
            self.tabela.insert("", "end", values=(f"{i+1}", f"Produto {i+1}", f"{10.50 * (i+1):.2f}", f"{i+10}"))
    
    def salvar(self):
        # Função para salvar o produto
        nome = self.nome_entry.get()
        descricao = self.descricao_text.get("1.0", "end-1c")
        
        # Validando preço
        try:
            preco = float(self.preco_entry.get())
        except ValueError:
            messagebox.showerror("Erro", "Preço inválido!")
            return
        
        # Validando quantidade
        try:
            quantidade = int(self.qtd_entry.get())
        except ValueError:
            messagebox.showerror("Erro", "Quantidade inválida!")
            return
        
        # Validação básica
        if not nome:
            messagebox.showerror("Erro", "Nome do produto é obrigatório!")
            return
        
        # Aqui implementaríamos a lógica para salvar no banco de dados
        
        messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
        self.limpar_campos()
    
    def limpar_campos(self):
        # Função para limpar os campos do formulário
        self.nome_entry.delete(0, "end")
        self.descricao_text.delete("1.0", "end")
        self.preco_entry.delete(0, "end")
        self.qtd_entry.delete(0, "end")
    
    def editar_produto(self):
        # Seleciona o item da tabela
        selecao = self.tabela.selection()
        if not selecao:
            messagebox.showwarning("Aviso", "Selecione um produto para editar!")
            return
            
        # Obter valores do item selecionado
        valores = self.tabela.item(selecao[0], "values")
        
        # Preencher campos com os valores atuais
        self.nome_entry.delete(0, "end")
        self.nome_entry.insert(0, valores[1])
        
        self.preco_entry.delete(0, "end")
        self.preco_entry.insert(0, valores[2])
        
        self.qtd_entry.delete(0, "end")
        self.qtd_entry.insert(0, valores[3])
    
    def excluir_produto(self):
        # Seleciona o item da tabela
        selecao = self.tabela.selection()
        if not selecao:
            messagebox.showwarning("Aviso", "Selecione um produto para excluir!")
            return
            
        # Confirmação de exclusão
        if messagebox.askyesno("Confirmar exclusão", "Tem certeza que deseja excluir o produto?"):
            # Aqui implementaríamos a lógica de exclusão no banco de dados
            self.tabela.delete(selecao)
            messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")