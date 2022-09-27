from flask import Flask, render_template, request
from flask_fontawesome import FontAwesome
import os

app = Flask(__name__)
fa = FontAwesome(app)


# Pagina inicial
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=('GET', 'POST'))
def login():
    x = {}
    if request.method == 'POST':
        n = request.form['email']
        s = request.form['senha']
        x['n'] = n
        x['s'] = s

    return render_template('login.html', tudo={x['n'], x['s']})


if __name__ == '__main__':
    port = int(os.getenv('PORT', '5000'))
    app.run('0.0.0.0', port=port)
