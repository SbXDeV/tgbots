import sqlite3
from pathlib import Path
from sqlite3 import Error


def db_create():
    try:
        connect = sqlite3.connect('sqlite_python.db')
        try:
            worker = connect.cursor()
            worker.execute("""
            CREATE TABLE IF NOT EXISTS list_user (
            id integer PRIMARY KEY,
            username varchar,
            first_name varchar,
            last_name varchar
            )
            """)
            connect.commit()
            connect.close()
        except Error as error:
            print('Ошибка создания базы данных: {}'.format(error))
    except Error as error:
        print('Ошибка подключения базы данных: {}'.format(error))


def db_insert(id, username, first_name, last_name):
    db_create()
    try:
        connect = sqlite3.connect('sqlite_python.db')
        worker = connect.cursor()
        project = worker.execute("""
                    SELECT EXISTS(SELECT id FROM list_user WHERE id={}) AS user_id_alias;
                    """.format(id))
        if project.fetchone()[0] == 1:
            print('Данные в базе данных уже имеются!')
            pass
        else:
            worker.execute("""
            INSERT INTO list_user(id, username, first_name, last_name) VALUES (?,?,?,?)
            """, (id, username, first_name, last_name))
            connect.commit()
            connect.close()
    except Error as error:
        print('Ошибка внесения данных: {}'.format(error))


def db_select():
    try:
        #get_absolute_path = '/root/code/tgbot/'
        #connect = sqlite3.connect(get_absolute_path + 'sqlite_python.db')
        connect = sqlite3.connect('sqlite_python.db')
        worker = connect.cursor()
        id_profile = worker.execute(''' SELECT id FROM list_user ''')
        rows = id_profile.fetchall()
        return rows
    except Error as error:
        print('Ошибка поиска данных: {}'.format(error))
