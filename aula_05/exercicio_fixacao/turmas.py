from os import path
from sqlite3 import dbapi2 as sqlite

db_filename = path.join(path.dirname(path.abspath(__file__)), 'exercise.db')


def insert():
    try:
        codigo = input('informe o codigo da turma: ')
        nome = input('informe o nome da turma: ')

        sql = 'insert into turmas (codigo, nome) values (?,?);'
        cx = sqlite.connect(db_filename)
        db_cur = cx.cursor()
        db_cur.execute(sql, [codigo, nome])
        cx.commit()
        print('turma registrado com sucesso.')
    except err:
        print(err)
    finally:
        db_cur.close()
        cx.close()


def update():
    try:
        codigo = input('informe o codigo da turma: ')
        nome = input('informe o nome da turma: ')

        sql = 'update turmas set nome = ? where codigo = ?;'
        cx = sqlite.connect(db_filename)
        db_cur = cx.cursor()
        db_cur.execute(sql, [nome, codigo])
        cx.commit()
        print('turma atualizada com sucesso.')
    except err:
        print(err)
    finally:
        db_cur.close()
        cx.close()


def delete():
    try:
        codigo = input('informe o código da turma: ')

        sql = 'delete from turmas where codigo = ?;'
        cx = sqlite.connect(db_filename)
        db_cur = cx.cursor()
        db_cur.execute(sql, [codigo])
        cx.commit()
        print('turma excluída com sucesso.')
    except err:
        print(err)
    finally:
        db_cur.close()
        cx.close()


def fetch():
    try:
        codigo = input('informe o código da turma: ')

        sql = 'select * from  turmas where codigo = ?;'
        cx = sqlite.connect(db_filename)
        db_cur = cx.cursor()
        db_cur.execute(sql, [codigo])
        obj = db_cur.fetchone()
        print(f'Turma {obj[2]} de código {obj[1]}')
    except err:
        print(err)
    finally:
        db_cur.close()
        cx.close()
