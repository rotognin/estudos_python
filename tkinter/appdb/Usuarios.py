from Banco import Banco

class Usuarios(object):
    def __init__(self, idusuario = 0, nome = "", telefone = "", email = "", usuario = "", senha = ""):
        self.info = {}
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha


    def insertUser(self):
        banco = Banco()
        try:

            conn = banco.conexao.cursor()

            conn.execute("INSERT INTO usuarios_tb (usu_nome, usu_telefone, usu_email, usu_login, usu_senha) VALUES ('" + 
                          self.nome + "', '" +
                          self.telefone + "', '" + self.email + "', '" +
                          self.usuario + "', '" + self.senha + "' )")

            banco.conexao.commit()
            conn.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):
        banco = Banco()
        try:

            conn = banco.conexao.cursor()

            conn.execute("UPDATE usuarios_tb SET usu_nome = '" + self.nome + "', usu_telefone = '" + 
                       self.telefone + "', usu_email = '" + self.email + "', usu_login = '" + 
                       self.usuario + "', usu_senha = '" + self.senha + "' where usu_id = " + self.idusuario + " ")

            banco.conexao.commit()
            conn.close()

            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):
        banco = Banco()
        try:

            conn = banco.conexao.cursor()

            conn.execute("DELETE FROM usuarios_tb WHERE usu_id = " + self.idusuario + " ")

            banco.conexao.commit()
            conn.close()

            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, idusuario):
        banco = Banco()
        try:

            conn = banco.conexao.cursor()

            conn.execute("SELECT * FROM usuarios_tb WHERE usu_id = " + idusuario + "  ")

            for linha in conn:
                self.idusuario = linha[0]
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]

            conn.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"