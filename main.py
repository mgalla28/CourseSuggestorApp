from flask import Flask, render_template
from Core.CourseList import CourseList
from Core.Course import Course
from MongoManager import MongoManager

app = Flask(__name__)


@app.route('/')
def main():
    dbManager = MongoManager()
    return render_template('main.html', classes=dbManager.get_courselist())


@app.route('/about')
def about_page():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()

