from os import path
from sqlite3 import dbapi2 as sqlite

db_filename = path.join(path.dirname(path.abspath(__file__)), 'mydb.db')
cx = sqlite.connect(db_filename)

db_curs = cx.cursor()

# db_curs.execute('''CREATE TABLE pessoas (
#                 id INTEGER PRIMARY KEY,
#                 nome VARCHAR(20));''')

# db_curs.execute('INSERT INTO pessoas(nome) VALUES (?);', ['joao'])


# try:
#     db_curs.execute('INSERT INTO pessoas(nome) VALUES (:nome);', ['maria'])
#     cx.commit()
# except sqlite.DatabaseError:
#     cx.rollback()


data = db_curs.execute('select * from pessoas where id = 5;')
row = db_curs.fetchone()

if row is None:
    print('Nenhum registro encontrado.')
else:
    print(row[0], row[1])


data = db_curs.execute('select * from pessoas;')
for row in data:
    print(row[0], row[1])
