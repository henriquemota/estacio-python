from tkinter import *


def insere():
    e.insert(INSERT, "*")


def limpa():
    e.delete(INSERT, END)


e = Entry(font="Arial 24")
i = Button(text="Insere*", command=insere)
l = Button(text="Limpa", command=limpa)
e.pack()
for w in (i, l):
    w.pack(side="left")
mainloop()
