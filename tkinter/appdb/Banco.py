import sqlite3

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        conn = self.conexao.cursor()
        conn.execute("""create table if not exists usuarios_tb(
                        usu_id integer primary key autoincrement,
                        usu_nome text,
                        usu_telefone text,
                        usu_email text,
                        usu_login text,
                        usu_senha text)""")
        self.conexao.commit()
        conn.close()