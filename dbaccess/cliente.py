class Cliente:
    def __init__(self, lista):
        self.cliID = int(lista[0])
        self.cliNome = str(lista[1])
        self.cliEmail = str(lista[2])

    def exibir(self):
        print('--- Cliente ---')
        print('Nome: ' + self.cliNome)
        print('E-mail: ' + self.cliEmail)