#!/usr/bin/env/python
# -*- coding: utf-8 -*-
from tkinter import *   #importa a bibioteca do TKinter
from tkinter import ttk 
root = Tk()             #cria a aplicação raiz. 
#w = Label(root, text="Teste TKinter!")    #cria um label com o texto especificado
#w.pack()                                      #insere na tela
ttk.Button(root, text="Hello World").grid()
root.mainloop()                               #inicializa o loop
