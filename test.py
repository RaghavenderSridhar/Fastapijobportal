print("hello world")
import psycopg2
from psycopg2 import sql    

db_name = "suppliers2"

con = psycopg2.connect(
                ##always make it 127.0.0.1
                host="127.0.0.1",
                # host="local",
                database="db_course",
                user="newuser",
                password="Bardock123$",
                port="5432")

print(con)

# cur = con.cursor()

# cur.execute(sql.SQL(f'CREATE DATABASE {sql.Identifier(db_name)}'))


# con = psycopg2.connect(
#                 host="127.0.0.1",
#                 database="suppliers2",
#                 user="raghavendersridhar",
#                 password="Bardock123$",
#                 port="5432")

print(con)

with con:

    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS cars")
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("DROP TABLE IF EXISTS test2")
    cur.execute("DROP TABLE IF EXISTS test3")
    cur.execute("CREATE TABLE test4(id SERIAL PRIMARY KEY, name VARCHAR(255), price INT)")
    cur.execute("INSERT INTO test4(name, price) VALUES('Audi', 7777)")
    cur.execute("INSERT INTO test4(name, price) VALUES('Mercedes', 6767)")
    cur.execute("INSERT INTO test4(name, price) VALUES('Skoda', 9000)")
    cur.execute("INSERT INTO test4(name, price) VALUES('Volvo', 29000)")
    cur.execute("INSERT INTO test4(name, price) VALUES('Bentley', 350000)")
    cur.execute("INSERT INTO test4(name, price) VALUES('Citroen', 21000)")
    cur.execute("INSERT INTO test4(name, price) VALUES('Hummer', 41400)")
    cur.execute("INSERT INTO test4(name, price) VALUES('Volkswagen', 21600)")
    cur.execute("INSERT INTO test4(name, price) VALUES('rgv', 21600)")

