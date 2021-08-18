from tkinter import *
import Aplicacao as app

root = Tk()
root.title = 'Aplicação de teste com opções'

tamanho, altura = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (tamanho, altura))
root.configure(background = "#eee")

#root.attributes('-fullscreen', True)
app.Application(root)
root.mainloop()