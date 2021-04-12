from os import path
from sqlite3 import dbapi2 as sqlite

db_filename = path.join(path.dirname(path.abspath(__file__)), 'exercise.db')


def initdb():
    try:
        tb_alunos = '''create table if not exists alunos (
                    id integer primary key,
                    matricula varchar(10) not null unique,
                    nome varchar(100) not null,
                    alunos datetime not null,
                    sexo char(1) not null
                    );'''

        tb_turmas = '''create table if not exists turmas (
                    id integer primary key,
                    codigo varchar(10) not null unique,
                    nome varchar(100) not null
                    );'''

        tb_matriculas = '''create table if not exists matriculas (
                    id integer primary key,
                    id_aluno integer not null references alunos (id),
                    id_turma integer not null references turmas (id),
                    ano int not null,
                    periodo int not null
                    );'''
        print('iniciando o banco de dados')
        cx = sqlite.connect(db_filename)
        print('iniciando o cursor')
        db_cur = cx.cursor()
        print('criando a tabela alunos')
        db_cur.execute(tb_alunos)
        print('criando a tabela turmas')
        db_cur.execute(tb_turmas)
        print('criando a tabela matriculas')
        db_cur.execute(tb_matriculas)
        cx.commit()
    except err:
        print(err)
    finally:
        db_cur.close()
        cx.close()
