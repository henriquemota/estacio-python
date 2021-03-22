import sys
from tkinter import *


class Application:

    def __init__(self, master=None):
        self.f = Frame(master)
        self.f.pack()
        self.l = Label(self.f, text="Prinmeiro widget")
        self.l.pack()
        self.b = Button(self.f, text='clique aqui', command=quit)
        self.b.pack()

    def quit():
        sys.exit()


w = Tk()
w.title('Primeiro app')
w.geometry('400x300')
Application(w)
w.mainloop()
