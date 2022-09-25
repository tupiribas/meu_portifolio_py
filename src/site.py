from flask import Flask, render_template
from flask_fontawesome import FontAwesome

site = Flask(__name__)
fa = FontAwesome(site)


# Pagina inicial
@site.route('/')
def index():
    return render_template('index.html')


@site.route('/cadastro')
def login():
    return render_template('login.html')


@site.route('/projetos')
def projetos():
    return render_template('projetos.html')


# Colocar o site no ar
if __name__ == "__main__":
    site.run(debug=True)
