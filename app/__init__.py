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


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/adm', methods=['POST'])
def areadoadm():
    n = request.form.get('email')
    s = request.form.get('senha')

    return "{} e {}".format(n, s)
    # return render_template('areaadm.html', tudo={x['n'], x['s']})


if __name__ == '__main__':
    port = int(os.getenv('PORT', '5000'))
    app.run('0.0.0.0', port=port)
