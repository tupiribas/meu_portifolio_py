from app import app
from flask import render_template


# Pagina inicial
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
