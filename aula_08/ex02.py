from tkinter import *


def inc():
    valor = int(label.configure('text')[4])
    label.configure(text=(valor + 1))


label = Label(None, text='0')
label.pack()
button = Button(None, text="Incrementar", command=inc)
button.pack()


mainloop()
