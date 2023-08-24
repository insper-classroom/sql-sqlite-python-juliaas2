import sqlite3

# Exercício de Python - Sqlite

# Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE Estudante')#para não rodar varias vezes 
cursor.execute("""
CREATE TABLE IF NOT EXISTS Estudante (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    AnoIngresso INTEGER
);
""")

estudante=[('Ana Silva','Computação',2019),
           ('Pedro Mendes', 'Física',2021),
           ('Carla Souza','Computação',2020),
           ('João Alves','Matemática',2018),
           ('Maria Oliveira','Química',2022)]

cursor.executemany("""
INSERT INTO Estudante (Nome, Curso, AnoIngresso)
VALUES (?, ?, ?);
""", estudante)

conn.commit()

cursor.execute("SELECT * FROM Estudante")

cursor.execute("SELECT * FROM Estudante WHERE AnoIngresso=2019 OR AnoIngresso=2020")
conn.commit()

cursor.execute("UPDATE Estudante SET AnoIngresso= ? WHERE Nome= ?", (2015, "Ana Silva"))
cursor.execute("SELECT * FROM Estudante")
conn.commit()

cursor.execute("DELETE FROM Estudante WHERE ID = ?", (1,))
cursor.execute("SELECT * FROM Estudante")
conn.commit()

cursor.execute("SELECT * FROM Estudante WHERE AnoIngresso>2019")
conn.commit()

cursor.execute("UPDATE Estudante SET AnoIngresso= ? WHERE Curso= ?", (2018, "Computação"))
cursor.execute("SELECT * FROM Estudante")
conn.commit()
print(cursor.fetchall())

# Vamos criar uma tabela chamada "Estudantes" com os seguintes campos:
# ID (chave primária) -  Criado automáticamente pela base de dados
# Nome
# Curso
# Ano de Ingresso

