from flask import Flask, render_template, request

numb = 0
app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')

@app.post('/submit')
def submit():
    numb = request.form.get('numb')
    return render_template('submit.html', numb=numb)