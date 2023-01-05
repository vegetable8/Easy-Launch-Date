from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route("/")
def hello():
    
    return render_template("index.html")

@app.route("/<name>")
def countDown(name):
    with sqlite3.connect('database.db') as conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM table')
        for row in cur:
            print(row)
            print(name)
        return render_template("index.html")


if __name__ == '__main__':
    app.run()


