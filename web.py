from flask import Flask, render_template, request
from numbers import sentence_maker
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/process", methods=['POST'])
def process():
    phn_num = int(request.form['phn_num'])
    data = sentence_maker(phn_num)
    return render_template('index.html', data=data, phn_num=phn_num)