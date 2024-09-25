from datetime import datetime
import sqlite3


db_path = "database/"

conn = sqlite3.connect('database//db.sqlite3')

sql_del = 'DELETE FROM remedio'
conn.execute(sql_del)
conn.commit()



sql = 'INSERT INTO remedio (nome, data_insercao) VALUES (?,?)'

dados = [
      ('Nesoldina', datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
      ("Discongex", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
      ("Multigrip", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
      ("Novalgina", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
      ("Tylenol Sinus", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
      ("Trezet", datetime.now().strftime("%Y-%m-%d %H:%M:%S")), 
]


conn.executemany(sql, dados)
conn.commit()
conn.close()
