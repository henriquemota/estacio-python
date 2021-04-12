from os import path
from sqlite3 import dbapi2 as sqlite
from datetime import datetime

db_filename = path.join(path.dirname(path.abspath(__file__)), 'exercise.db')


def insert():
    try:
        matricula = input('informe sua matricula: ')
        nome = input('informe seu nome: ')
        nascimento = input('informe seu nascimento: ')
        sexo = input('informe seu sexo: ')

        sql = 'insert into alunos (matricula, nome, nascimento, sexo) values (?,?,?,?);'
        cx = sqlite.connect(db_filename)
        db_cur = cx.cursor()
        db_cur.execute(sql, [matricula, nome, nascimento, sexo])
        cx.commit()
        print('aluno registrado com sucesso.')
    except err:
        print(err)
    finally:
        db_cur.close()
        cx.close()


def fetch():
    try:
        matricula = input('informe sua matricula: ')

        sql = 'select * from  alunos where matricula = ?;'
        cx = sqlite.connect(db_filename)
        db_cur = cx.cursor()
        db_cur.execute(sql, [matricula])
        obj = db_cur.fetchone()
        print(f'Aluno {obj[2]}, matrícula {obj[1]} - sexo {obj[4]}')
    except err:
        print(err)
    finally:
        db_cur.close()
        cx.close()
