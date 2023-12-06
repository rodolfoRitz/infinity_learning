from sqlite3 import connect

conexao = connect(database="loja.db")

cursor = conexao.cursor()

dados = cursor.execute("PRAGMA table_info(clientes)").fetchall()

print([d[1] for d in dados])