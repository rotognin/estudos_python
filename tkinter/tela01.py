from tkinter import *

class Application:
    def __init__(self, master = None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text = 'Primeiro widget')
        self.msg["font"] = ('Verdana', '10', 'italic', 'bold')
        self.msg.pack(side = RIGHT)
        self.sair = Button(self.widget1)
        self.sair['text'] = 'Sair'
        self.sair['font'] = ('Calibri', '10')
        self.sair['width'] = 5
        #self.sair['command'] = self.widget1.quit

        # Podemos atribuir o event de dar clique com o mouse, ou 
        # atribuir uma função a ser chamada pelo evento próprio do
        # botão ('command')

        #self.sair.bind('<Button-1>', self.mudarTexto)

        self.sair['command'] = self.mudarTexto

        self.sair.pack(side = RIGHT)

    # Nota: Se usado o "bind" para chamar essa função, o segundo argumento
    # deverá ser o "event": def mudarTexto(self, event)
    def mudarTexto(self):
        if (self.msg['text'] == 'Primeiro widget'):
            self.msg['text'] = 'Mudou o texto'
        else:
            self.msg['text'] = 'Primeiro widget'



root = Tk()
Application(root)
root.mainloop()

