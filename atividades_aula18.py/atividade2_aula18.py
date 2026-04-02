import tkinter as tk
from tkinter import messagebox

# Função para enviar os dados
def enviar_dados():
    nome = entry_nome.get()
    idade = entry_idade.get()
    email = entry_email.get()
    endereco = entry_endereco.get()
    celular = entry_celular.get()
    cep = entry_cep.get()
    cidade = entry_cidade.get()
    cursos = entry_cursos.get()

    # Impressão no console
    print("===== DADOS DO CLIENTE =====")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"E-mail: {email}")
    print(f"Endereço: {endereco}")
    print(f"Celular: {celular}")
    print(f"CEP: {cep}")
    print(f"Cidade: {cidade}")
    print(f"Cursos: {cursos}")
    print("============================")

    messagebox.showinfo("Sucesso", "Dados enviados com sucesso!")

# Criando a janela principal
janela = tk.Tk()
janela.title("Cadastro de Clientes")
janela.geometry("1700x750")

# Título
titulo = tk.Label(janela, text="Formulário de Cadastro de Clientes", font=("Arial", 20))
titulo.pack(pady=20)

# Frame para organizar os campos
frame = tk.Frame(janela)
frame.pack(pady=20)

# Função para criar labels e entradas
def criar_campo(texto, linha):
    label = tk.Label(frame, text=texto, font=("Arial", 12))
    label.grid(row=linha, column=0, padx=10, pady=10, sticky="w")
    entry = tk.Entry(frame, width=50)
    entry.grid(row=linha, column=1, padx=10, pady=10)
    return entry

# Criando os campos
entry_nome = criar_campo("Nome:", 0)
entry_idade = criar_campo("Idade:", 1)
entry_email = criar_campo("E-mail:", 2)
entry_endereco = criar_campo("Endereço:", 3)
entry_celular = criar_campo("Celular:", 4)
entry_cep = criar_campo("CEP:", 5)
entry_cidade = criar_campo("Cidade:", 6)
entry_cursos = criar_campo("Cursos:", 7)

# Botão de enviar
botao_enviar = tk.Button(janela, text="Enviar", font=("Arial", 14), command=enviar_dados)
botao_enviar.pack(pady=20)

# Rodando a aplicação
janela.mainloop()
