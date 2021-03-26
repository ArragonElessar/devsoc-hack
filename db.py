from psycopg2 import *
from random import randint

host = 'ec2-52-1-115-6.compute-1.amazonaws.com'
dbname = 'dd0n7ifl5576p3'
user = 'ianetcwtdkuevw'
port = '5432'
password = 'cb0aff90448585e38776ae67266ebe2ea3b5bd7760895050028571f954153863'

conn = connect(dbname=dbname, user=user, port=port, password=password, host=host)
cur = conn.cursor()


# """create table users(id bigint not null primary key ,name varchar(256), email varchar(256), password varchar(256))"""
def check(email):
    q = f"""select * from users where email='{email}'"""
    cur.execute(q)
    table = cur.fetchall()
    print(table)
    if len(table) > 0:
        return False
    else:
        return True


def register_user(name, email, password):
    if check(email):
        q = """INSERT INTO users (id, name, email, password) VALUES (%s, %s, %s, %s)"""
        record = (randint(0, 1000), name, email, password)
        cur.execute(q, record)
        conn.commit()
        return True
    else:
        return False


def log_user_in(email, password):
    q = f"""select password from users where email='{email}'"""
    cur.execute(q)
    got_pass = cur.fetchall()
    if got_pass[0][0] == password:
        return True
    else:
        return False


def truncate():
    q = """truncate table users"""
    cur.execute(q)
    conn.commit()


def view():
    q = """select * from users"""
    cur.execute(q)
    table = cur.fetchall()
    print(table)

view()
