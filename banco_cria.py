import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

#criar_tabela = "CREATE TABLE IF NOT EXISTS valores (id_id text PRIMARY KEY, \
#     valor_atual float, ultimo_ganho float, ultimo_gasto float)"

#cria_hoteis = "INSERT INTO valores VALUES ('1', 1200, 200, 75)"


connection.commit()
connection.close()