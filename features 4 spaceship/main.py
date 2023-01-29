from flask import Flask, render_template, request
from quantum_backend import data
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('index.html', data = data)



