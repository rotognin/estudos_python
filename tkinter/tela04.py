# Testes utilizando o gerenciador de posições "grid"
# Site para referência: https://cadernodelaboratorio.com.br/tkinter-conhecendo-o-grid-em-maiores-detalhes/

from tkinter import *
from tkinter import messagebox

class Application:
    def __init__(self, master = None):
        self.quadro = Frame(master, pady = 10, padx = 10)
        
        self.frmInfo = Frame(self.quadro)
        # Nome
        self.lblNome = Label(self.frmInfo, text = 'Nome:')
        self.entNome = Entry(self.frmInfo, width = 50)
        # Endereço
        self.lblEndereco = Label(self.frmInfo, text = 'Endereço:')
        self.entEndereco = Entry(self.frmInfo, width = 50)

        # Botões
        self.frmBotoes = Frame(self.quadro)
        self.btnAdicionar = Button(self.frmBotoes, text = 'Adicionar', width = 9, command = self.adicionarInfo)
        self.btnExcluir = Button(self.frmBotoes, text = 'Excluir', width = 9, command = self.excluirInfo)
        self.btnLimpar = Button(self.frmBotoes, text = 'Limpar', width = 9, command = self.limparInfo)

        # ListBox
        self.frmLista = Frame(self.quadro)
        self.lbxLista = Listbox(self.frmLista, selectbackground = 'blue', selectmode = SINGLE, width = 100, activestyle = 'none')
        #self.btnSair = Button(self.quadro, text = 'Sair', width = 10, command = self.quadro.quit)

    def criarTela(self):
        self.frmInfo.grid(row = 0, column = 0)
        self.quadro.grid(row = 0, column = 0)
        self.lblNome.grid(row = 0, column = 0, sticky = W) # Alinhado à esquerda (E = à direita)
        self.entNome.grid(row = 0, column = 1, sticky = W)
        self.lblEndereco.grid(row = 1, column = 0, sticky = W)
        self.entEndereco.grid(row = 1, column  = 1, sticky = W)

        self.frmBotoes.grid(row = 2, column = 0, sticky = 'nsew', padx = 5, pady = 5)
        self.btnAdicionar.pack(side = 'left', padx = 5)
        self.btnLimpar.pack(side = 'left', padx = 5)
        self.btnExcluir.pack(side = 'left', padx = 5)

        #self.btnAdicionar.grid(row = 2, column = 0, sticky = W, pady = 5)
        #self.btnLimpar.grid(row = 2, column = 1, sticky = W, padx = 5)
        #self.btnExcluir.grid(row = 2, column = 1, sticky = W)

        self.frmLista.grid(row = 3, column = 0, columnspan = 3)
        self.lbxLista.pack() # grid(row = 0, column = 0, sticky = E, pady = 5)
        self.lbxLista.bind('<<ListboxSelect>>', self.itemSelecionado)


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

    def limparInfo(self):
        self.lbxLista.delete(0, END)
        self.entNome.focus_set()

    def excluirInfo(self):
        iIndex = self.lbxLista.curselection()
        if (iIndex == ()):
            messagebox.showwarning('Atenção', 'É necessário selecionar um registro para exclusão.')
            return

        self.lbxLista.delete(iIndex)

    def limparCampos(self):
        self.entNome.delete(0, END)
        self.entEndereco.delete(0, END)
        self.entNome.focus_set()

    def itemSelecionado(self, event):
        iIndex = self.lbxLista.curselection()
        if (not iIndex == ()):
            messagebox.showinfo('Selecionado', self.lbxLista.get(iIndex))



root = Tk()

tamanho, altura = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (tamanho, altura))
root.configure(background = "#eee")
root.title('Operações diversas')

app = Application(root)
app.criarTela()
root.mainloop()