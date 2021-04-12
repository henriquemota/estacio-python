from os import path
from sqlite3 import dbapi2 as sqlite

db_filename = path.join(path.dirname(path.abspath(__file__)), 'exercise.db')


def initdb():
    try:
        tb_nascimento = '''create table if not exists alunos (
                            id integer primary key,
                            matricula varchar(10) not null unique,
                            nome varchar(100) not null,
                            nascimento datetime not null,
                            sexo char(1) not null
                          );'''
        print('iniciando o banco de dados')
        cx = sqlite.connect(db_filename)
        print('iniciando o cursor')
        db_cur = cx.cursor()

        print('criando a tabela do banco de dados')
        db_cur.execute(tb_nascimento)
    except err:
        print(err)
    finally:
        db_cur.close()
        cx.close()
