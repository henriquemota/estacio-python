import os
from os import path
from sqlite3 import dbapi2 as sqlite


def importacao():
  csv_filepath = path.join(path.dirname(path.abspath(__file__)), "dataset.csv")
  db_filename = path.join(path.dirname(path.abspath(__file__)), "database.db")

  with sqlite.connect(db_filename) as cx:
      db_curs = cx.cursor()
      db_curs.execute(
          """CREATE TABLE IF NOT EXISTS dados (
                    id INTEGER PRIMARY KEY,
                    regiao varchar(100),
                    estado varchar(2),
                    data date,
                    casos_novos int,
                    casos_acumulados int,
                    obitos_novos int,
                    obitos_acumulados int);"""
      )

      try:
          with open(csv_filepath) as file:
              for line in file.readlines():
                  cols = line.split(";")
                  db_curs.execute(
                      """
                    INSERT INTO dados
                    (regiao, estado, casos_novos, casos_acumulados, obitos_novos, obitos_acumulados)
                    VALUES
                    (?,?,?,?,?,?);""",
                      [cols[0], cols[1], cols[3], cols[4], cols[5], cols[6]],
                  )
                  cx.commit()
              print("tudo ok")
      except sqlite.DatabaseError, e:
          print(str(e))
          cx.rollback()
          print("tudo errado")

db_filename = path.join(path.dirname(path.abspath(__file__)), "database.db")
with sqlite.connect(db_filename) as cx:
    db_curs = cx.cursor()
    result = db_curs.execute("select estado, count(casos_acumulados) as total from dados group by estado;");
    for line in result:
      print(line)

