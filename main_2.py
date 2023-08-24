import db_utils
import sqlite3

conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()


tabela =db_utils.tabela('Estudantes',"(ID INTEGER PRIMARY KEY AUTOINCREMENT, Nome TEXT NOT NULL, Curso TEXT NOT NULL, AnoIngresso INTEGER)", [('Ana Silva', 'Computação', 2019),('Pedro Mendes', 'Física', 2021),('Carla Souza', 'Computação', 2020),('João Alves', 'Matemática', 2018),('Maria Oliveira', 'Química', 2022)])

filtro= db_utils.filtra('Estudantes', 'AnoIngresso', 2019, 2020)

atualizar = db_utils.update('Estudantes', 'AnoIngresso', 2020, 'Nome', 'Ana Silva')

deletar = db_utils.delete('Estudantes', 'ID', 5)

filtrar_ano= db_utils.filtracurso('Estudantes', 'AnoIngresso', 2014, 'Curso', 'Computação')

Update = db_utils.update('Estudantes', 'AnoIngresso', 2020, 'Curso', 'Computação')

conn.close()