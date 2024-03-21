from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Olá mundo', 200


def autenticar(user, senha):
    return True

@app.route('/dashboard')
def not_found():
    user = 'abc'
    senha = '123'
    if not autenticar(user, senha):
        return 'Não autorizado'



if __name__ == '__main__':
    app.run(debug=True)