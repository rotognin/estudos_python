import sqlite3

class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('podcasts.db')
        self.createTable()

    def createTable(self):
        conn = self.conexao.cursor()
        conn.execute("""create table if not exists 99vidas_tb(
                        99v_id integer primary key autoincrement,
                        99v_titulo text,
                        99v_arquivo text,
                        99v_datahora text)""")
        self.conexao.commit()
        conn.close()

    def insertEpisodio(self, conn, titulo, arquivo, datahora):
        try:
            sSql = 'INSERT INTO 99vidas_tb (99v_titulo, 99v_arquivo, 99v_datahora)'
            sSql = sSql + ' VALUES ('
            sSql = sSql + '"' + titulo + '", "' + arquivo + '", "' + datahora + '");'
            conn.execute(sSql)
            
            return True
        except:
            return False
