import sqlite3
def initDb():
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE 'countdowns' ('id'	INTEGER NOT NULL, 'route'	TEXT NOT NULL UNIQUE, 'title'	TEXT NOT NULL, 'endDate'	TEXT NOT NULL,'pictureName'	TEXT UNIQUE, PRIMARY KEY('id' AUTOINCREMENT));")
        conn.commit()
        print("Created table")
initDb()