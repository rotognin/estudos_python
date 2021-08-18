# Testes utilizando o gerenciador de posições "grid"
# Site para referência: https://cadernodelaboratorio.com.br/tkinter-conhecendo-o-grid-em-maiores-detalhes/

from tkinter import *

class Application:
    def __init__(self, master = None):
        self.quadro = Frame(master, pady = 10, padx = 10)
        
        self.lblNome = Label(self.quadro, text = 'Nome:')
        self.entNome = Entry(self.quadro, width = 50)
        self.lblEndereco = Label(self.quadro, text = 'Endereço:')
        self.entEndereco = Entry(self.quadro, width = 50)
        self.btnSair = Button(self.quadro, text = 'Sair', width = 10, command = self.quadro.quit)

        self.quadro.grid(row = 0, column = 0)
        self.lblNome.grid(row = 0, column = 0, sticky = W) # Alinhado à esquerda (E = à direita)
        self.entNome.grid(row = 0, column = 1)
        self.lblEndereco.grid(row = 1, column = 0, sticky = W)
        self.entEndereco.grid(row = 1, column  = 1)
        self.btnSair.grid(row = 2, column = 2)

app = Tk()
Application(app)
app.mainloop()