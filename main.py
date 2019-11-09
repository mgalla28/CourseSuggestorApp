from flask import Flask, render_template
from CourseList import CourseList
from pymongo import MongoClient
from os import system

app = Flask(__name__)


@app.route('/')
def main():

    conn = MongoClient()
    db = conn.ClassGraphs
    coll = db.CsClasses
    return render_template('main.html', classes=CourseList(coll).return_vertices())

@app.route('/about')
def about_page():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()
