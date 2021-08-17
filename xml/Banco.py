import sqlite3

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('podcasts.db')
        self.createTable()

    def createTable(self):
        conn = self.conexao.cursor()
        conn.execute("""create table if not exists cast99vidas_tb(
                        v99_id integer primary key autoincrement,
                        v99_titulo text,
                        v99_arquivo text,
                        v99_datahora text)""")
        self.conexao.commit()
        conn.close()

    def insertEpisodio(self, titulo, arquivo, datahora):
        try:
            cursor = self.conexao.cursor()
            sSql = 'INSERT INTO cast99vidas_tb (v99_titulo, v99_arquivo, v99_datahora)'
            sSql = sSql + ' VALUES ('
            sSql = sSql + '"' + titulo + '", "' + arquivo + '", "' + datahora + '");'
            cursor.execute(sSql)
            self.conexao.commit()
            
            return True
        except:
            return False
