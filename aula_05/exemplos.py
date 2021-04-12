from os import path
from sqlite3 import dbapi2

db_file = path.join(path.dirname(path.abspath(__file__)), 'mydb.db')
cx = dbapi2.connect(db_file)

cursor = cx.cursor()

# cursor.execute('insert into posts (title, content) values (:title,:content)',
#                {'title': 'mais um titulo', 'content': 'mais um conteudo'})
# cx.commit()

data = cursor.execute(
    'select * from posts where title = ?;', ['mais um titulo'])
rows = data.fetchall()
cursor.close()
cx.close()

for row in rows:
    print(row[1])
