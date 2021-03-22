import sys
from tkinter import *


def quit():
    sys.exit()


def main():
    w = Tk()
    w.title('Minha primeira janela Python')
    w.geometry('400x300')

    l = Label(w, text='Meu texto aqui')
    l.pack()

    b = Button(w, text='Clique aqui', command=quit)
    # b['text'] = 'clique aqui'
    # b['command'] = quit
    b.pack()

    w.mainloop()


main()
