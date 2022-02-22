from flask import Flask, render_template, request

app = Flask(__name__)

dict = {}
student = []
org = []

@app.get('/')
def index():
    return render_template('index.html', student=student)

@app.post('/submit')
def submit():
    student = request.form.get('student', 'Nothing')
    org = request.args.get('org')
    dict[student] = org
    return render_template('submit.html', student=student, dict=dict)
