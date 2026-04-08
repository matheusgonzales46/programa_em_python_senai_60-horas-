import sqlite3 # banco de dados
import tkinter as tk # lib de interface gráfica
from tkinter import messagebox, ttk # caixa de msg / tkinter


def conectar():
    return sqlite3.connect('teste.db')

# CREATE READ UPDATE DELETE

# banco de dados
def criar_tabela():
    conn = conectar()
    c = conn.cursor() # digitar sql num arquivo python
    c.execute('''
               CREATE TABLE IF NOT EXISTS usuarios(
             
              id INTEGER NOT NULL,
              nome TEXT NOT NULL,
              email TEXT NOT NULL
             
              )''')
    conn.commit()
    conn.close()          





# interface grafica
janela = tk.Tk()
janela.geometry('650x500')
janela.title('...CRUD...')

style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', background = 'white', font = ('arial', 10))
style.configure('TEntry', font = ('Segoe UI', 10))
style.configure('TButton', font = ('Segoe UI', 10), padding = 6)
style.configure('Treeview.Hending', font = ('Segoe UI', 10, 'bold'))
style.configure('Treeview',font = ('Segoe UI', 10, 'bold'))


# frames  -  sessão
main_frame =  ttk.Frame(janela, padding=15)
main_frame.pack(fill=tk.BOTH, expand=True)


# widgets -  elementos
titulo = ttk.Label(main_frame, text='Sistema de Cadastro', font=('Segoe UI', 10, 'bold'))
titulo.grid(row=0, columnspan=2,pady=(0,15), sticky='w')

input_frame =  ttk.LabelFrame(main_frame, text='DADOS DO USUARIO', padding=10)
input_frame.grid(row=1,column= 0, columnspan = 2, sticky='ew', pady=(0,15))

# textos para direcionar
# CPF
ttk.Label(input_frame, text='CPF').grid(row=0, column=0, padx=(0,10), pady=5, sticky='e')

entry_cpf = ttk.Entry(input_frame, width=30)
entry_cpf.grid(row=0, column=1, padx=(0,20), pady=5, sticky='w')

# textos para direcionar
# NOME
ttk.Label(input_frame, text='NOME').grid(row=1, column=0, padx=(0,10), pady=5, sticky='e')

entry_nome = ttk.Entry(input_frame, width=30)
entry_nome.grid(row=1, column=1, padx=(0,20), pady=5, sticky='w')


# textos para direcionar
# NOME
ttk.Label(input_frame, text='E-MAIL').grid(row=2, column=0, padx=(0,10), pady=5, sticky='e')

entry_email = ttk.Entry(input_frame, width=30)
entry_email.grid(row=2, column=1, padx=(0,20), pady=5, sticky='w')

btn_frame = ttk.Frame(main_frame)
btn_frame.grid(row=2, column=0, columnspan=2, pady=(0,15), sticky='w')




btn_salvar = ttk.Button(btn_frame, text='SALVAR')
btn_salvar.pack(side = tk.LEFT, padx=5)



btn_salvar = ttk.Button(btn_frame, text='ATUALIZAR')
btn_salvar.pack(side = tk.LEFT, padx=5)




btn_salvar = ttk.Button(btn_frame, text='DELETAR')
btn_salvar.pack(side = tk.LEFT, padx=5)




btn_salvar = ttk.Button(btn_frame, text='LIMPAR')
btn_salvar.pack(side = tk.LEFT, padx=5)


tree_frame = ttk.Frame(main_frame)
tree_frame.grid(row=3, column=0, columnspan=2, sticky='nsew')

main_frame.columnconfigure(0,weight = 1)
main_frame.rowconfigure(3,weight = 1)

columns = ('ID', 'NOME', 'EMAIL' )
tree = ttk.Treeview(tree_frame, columns=columns, show='headings', height=12)
tree.pack(fill=tk.BOTH, expand=True)

for col in collumns:
    tree.heading(col, test= col)
    tree.column(col, width=180, anchor='center')

scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

















janela.mainloop()