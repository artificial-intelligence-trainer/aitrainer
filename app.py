from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/education')
def education():
    return render_template("education.html")


@app.route('/resources')
def resources():
    return render_template("resources.html")


@app.route('/teachers')
def teachers():
    return render_template("teachers.html")


@app.route('/master_classes')
def master_classes():
    return render_template("master-classes.html")


@app.route('/course')
def course():
    return render_template("course.html")


if __name__ == "__main__":
    app.run(debug=True)
