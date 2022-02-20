#cloned, then modified from Jacob Krevat in class example
from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

now = datetime.datetime.now()
current_time = now.strftime("%m/%d/%Y %a %H:%M")

@app.get('/')
def index():
    return render_template('index.html', name=current_time)



