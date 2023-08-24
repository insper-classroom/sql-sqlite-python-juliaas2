import sqlite3

conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

def tabela(nome, campos_tabela, dados):
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {nome} {campos_tabela};')
    conn.commit()
    cursor.executemany(f'INSERT INTO {nome} (Nome, Curso, AnoIngresso) VALUES (?, ?, ?);', dados)
    conn.commit()
    cursor.execute(f'SELECT * FROM {nome}')
    print(cursor.fetchall())


def filtra(nome, campo, restricao, restri):
    cursor.execute(f'SELECT * FROM {nome} WHERE {campo}={restricao} OR {campo}={restri}')
    print(cursor.fetchall())


def update(nome, set, restricao_set, where, restricao_where):
    cursor.execute(f'UPDATE {nome} SET {set}=? WHERE {where}=?', (restricao_set, restricao_where))
    conn.commit()
    cursor.execute(f'SELECT * FROM {nome}')
    print(cursor.fetchall())


def delete(nome, campo, restricao):
    cursor.execute(f'DELETE FROM {nome} WHERE {campo}={restricao}')
    conn.commit()
    cursor.execute(f'SELECT * FROM {nome}')
    print(cursor.fetchall())

def filtracurso(nome, campo, camp, restricao, restri):
    query = f'SELECT * FROM {nome} WHERE {campo} > ? AND {camp} = ?'
    cursor.execute(query, (restricao, restri))
    result = cursor.fetchall()
    for row in result:
        print(row)