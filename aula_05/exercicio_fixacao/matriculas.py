from os import path
from sqlite3 import dbapi2 as sqlite

db_filename = path.join(path.dirname(path.abspath(__file__)), 'exercise.db')


def insert():
    try:
        matricula = input('informe a matricula do aluno: ')
        codigo = input('informe o codigo da turma: ')
        ano = input('informe o ano: ')
        periodo = input('informe periodo: ')

        slqAluno = 'select * from alunos where matricula = ?;'
        db_cur.execute(sql, [matricula])
        aluno = db_cur.fetchone()

        slqTurma = 'select * from turmas where codigo = ?;'
        db_cur.execute(sql, [codigo)
        turma = db_cur.fetchone()

        sql = 'insert into matriculas (id_aluno, id_turma, ano, periodo) values (?,?,?,?);'
        cx = sqlite.connect(db_filename)
        db_cur = cx.cursor()
        db_cur.execute(sql, [aluno[0], turma[0], ano, periodo])
        cx.commit()
        print('matricula registrado com sucesso.')
    except err:
        print(err)
    finally:
        db_cur.close()
        cx.close()
