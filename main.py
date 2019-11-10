from flask import Flask, render_template
from CourseList import CourseList
from Course import Course
from pymongo import MongoClient
from os import system

app = Flask(__name__)


@app.route('/')
def main():

    conn = MongoClient()
    db = conn.ClassGraphs
    coll = db.CsClasses
    input_dict = dict()
    for i in coll.find({}):
        dep_str = i['dependents']  # type: str
        dep_list = dep_str.split(",")
        input_dict[i['designation']] = Course(i['designation'], dep_list, i['credit_hours'])

    return render_template('main.html', classes=CourseList(input_dict).return_vertices())

@app.route('/about')
def about_page():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()