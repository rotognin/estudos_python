from tkinter import Checkbutton, LabelFrame


from tkinter import *

class Application:
    def __init__(self, master = None):
        self.frameOpc = LabelFrame(master, text = 'Opções', relief = 'sunken', borderwidth = 1)
        self.frameOpc.pack(padx = 10, pady = 10, side = 'top')
        
        self.checkDelphi = Checkbutton(self.frameOpc, text = 'Delphi')
        self.checkDelphi.pack(side = LEFT)

        self.checkPython = Checkbutton(self.frameOpc, text = 'Python')
        self.checkPython.pack(side = LEFT)

        self.checkCobol = Checkbutton(self.frameOpc, text = 'Cobol')
        self.checkCobol.pack(side = LEFT)

        self.btnSair = Button(self.frameOpc, text = 'Sair', width = 20)
        self.btnSair['command'] = self.frameOpc.quit
        self.btnSair.pack(padx = 3, pady = 3, side = 'bottom')


