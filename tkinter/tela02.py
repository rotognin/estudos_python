from tkinter import *

class Application:
    def __init__(self, master = None):
        self.fontePadrao = ('Arial', '10')

        self.container1 = Frame(master)
        self.container1['pady'] = 10
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2['padx'] = 20
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3['padx'] = 20
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4['pady'] = 20
        self.container4.pack()

        self.titulo = Label(self.container1, text = 'Dados do usuário')
        self.titulo['font'] = ('Arial', '10', 'bold')
        self.titulo.pack()

        self.nomeLabel = Label(self.container2, text = 'Nome', font = self.fontePadrao)
        self.nomeLabel.pack(side = LEFT)

        self.nome = Entry(self.container2)
        self.nome['width'] = 30
        self.nome['font'] = self.fontePadrao
        self.nome.pack(side = LEFT)

        self.senhaLabel = Label(self.container3, text = 'Senha', font = self.fontePadrao)
        self.senhaLabel.pack(side = LEFT)

        self.senha = Entry(self.container3)
        self.senha['width'] = 30
        self.senha['font'] = self.fontePadrao
        self.senha['show'] = '*'
        self.senha.pack(side = LEFT)

        self.autenticar = Button(self.container4)
        self.autenticar['text'] = 'Autenticar'
        self.autenticar['font'] = ('Calibri', '8')
        self.autenticar['width'] = 12
        self.autenticar['command'] = self.verificarSenha
        self.autenticar.pack()

        self.mensagem = Label(self.container4, text = '', font = self.fontePadrao)
        self.mensagem.pack()

    # Método para verificar a senha
    def verificarSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()

        if (usuario == 'admin') and (senha == '123'):
            self.mensagem['text'] = 'Usuário autenticado!'
        else:
            self.mensagem['text'] = 'Usuário ou senha incorretos.'

root = Tk()
Application(root)
root.mainloop()
