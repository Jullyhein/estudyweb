from flask import Flask, request, redirect, render_template
from pprint import pprint

app = Flask(__name__)

@app.route('/cadastro', methods=['post'])
def cadastro():
    pprint(request.form)
    dicionario = dict(request.form)
    dicionario['nova-chave'] = 'novo valor da chave'
    return render_template("sucesso.html")

if __name__ == '__main__':
    app.run(debug=True)