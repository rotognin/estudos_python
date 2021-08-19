# Testes utilizando o gerenciador de posições "grid"
# Site para referência: https://cadernodelaboratorio.com.br/tkinter-conhecendo-o-grid-em-maiores-detalhes/

from tkinter import *
from tkinter import messagebox

class Application:
    def __init__(self, master = None):
        self.quadro = Frame(master, pady = 10, padx = 10)
        
        # Nome
        self.lblNome = Label(self.quadro, text = 'Nome:')
        self.entNome = Entry(self.quadro, width = 50)
        # Endereço
        self.lblEndereco = Label(self.quadro, text = 'Endereço:')
        self.entEndereco = Entry(self.quadro, width = 50)
        # Botão "Adicionar"
        self.btnAdicionar = Button(self.quadro, text = 'Adicionar', width = 10, command = self.adicionarInfo)
        # ListBox
        self.lbxLista = Listbox(self.quadro, selectbackground = 'blue', selectmode = SINGLE, width = 40)
        #self.lbxLista.insert(1, ('Rodrigo Tognin', 'João Henrique'))
        #self.lbxLista.insert(2, 'Tatiane da Silva')
        #self.btnSair = Button(self.quadro, text = 'Sair', width = 10, command = self.quadro.quit)

    def criarTela(self):
        self.quadro.grid(row = 0, column = 0)
        self.lblNome.grid(row = 0, column = 0, sticky = W) # Alinhado à esquerda (E = à direita)
        self.entNome.grid(row = 0, column = 1)
        self.lblEndereco.grid(row = 1, column = 0, sticky = W)
        self.entEndereco.grid(row = 1, column  = 1)
        self.btnAdicionar.grid(row = 2, column = 0, sticky = W)
        self.lbxLista.grid(row = 3, column = 0, columnspan = 2, sticky = W, pady = 5)
        self.entNome.focus_set()

        #self.btnSair.grid(row = 2, column = 2)

    def adicionarInfo(self):
        if (self.entNome.get() == ''):
            messagebox.showwarning('Atenção', 'O nome está em branco!')
            return

        if (self.entEndereco.get() == ''):
            messagebox.showwarning('Atenção', 'O endereço está em branco!')
            return

        self.lbxLista.insert(END, self.entNome.get() + ' - ' + self.entEndereco.get())
        self.limparCampos()

    def limparCampos(self):
        self.entNome.delete(0, END)
        self.entEndereco.delete(0, END)
        self.entNome.focus_set()



root = Tk()

tamanho, altura = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (tamanho, altura))
root.configure(background = "#eee")

app = Application(root)
app.criarTela()
root.mainloop()