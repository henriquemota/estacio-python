from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.a = Label(self, text='A')
        self.a.pack(side=TOP, expand=True, fill=X)
        self.b = Label(self, text='B')
        self.b.pack(side=LEFT, expand=True)

        for w in (self.a, self.b):
            w.configure(relief='groove')

        self.pack()


x = Application()
x.master.title('Alterando configuração')

mainloop()
