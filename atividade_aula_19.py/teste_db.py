
import sqlite3
import tkinter as tk



def salvar():
    c  =  sqlite3.connect('dados.db')
    cur =  c.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS dado(nome TEXT)')
    cur.execute('INSERT INTO dado(nome) VALUES (?)', (entrada.get(),))
    
    c.commit()
    c.close()

    entrada.delete(0,tk.END)

janela  =  tk.Tk()
janela.geometry('300x300')


entrada =  tk.Entry(janela, font=('arial', 25))
entrada.pack()


btn = tk.Button(janela, text =' clique aqui', font=('arial', 25),command=salvar)
btn. pack()


janela.mainloop()