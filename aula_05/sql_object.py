from sqlobject import *
from os import path
from sqlite3 import dbapi2 as sqlite
import datetime

db_filename = path.join(path.dirname(path.abspath(__file__)), 'mydb.db')

# cx = sqlite.connect(db_filename)
# db_curs = cx.cursor()
# db_curs.execute("""CREATE TABLE people(
#               id INTEGER PRIMARY KEY, first_name VARCHAR(20),
#               last_name VARCHAR(30), date_of_birth DATE)""")

# abre uma conexao com banco de dados
sqlhub.processConnection = connectionForURI(f'sqlite:{db_filename}')

# define o objeto que representa a tabela no banco de dados


class Person(SQLObject):
    class sqlmeta:
        table = 'people'
    firstName = StringCol(length=20)
    lastName = StringCol(length=30)
    dateOfBirth = DateCol()


# # insere o registro no banco de dados
# cecil = Person(firstName='Henrique', lastName='Mota',
#                dateOfBirth=datetime.date(1974, 10, 24))

# obj = Person.selectBy(firstName='Henrique')
obj = Person.select()
print(obj)
