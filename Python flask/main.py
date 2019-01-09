from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = 'Senha'

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1=Jogo('Mario', 'acao', 'nintendo')
jogo2=Jogo('pk', 'rpg', 'nintendo')
lista = [jogo1, jogo2]

@app.route('/')
def bem_vindo():
    return render_template('index.html', titulo='Olá', jogos = lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo="Novo Jogo")

@app.route('/criar', methods=['POST',])
def criar():
    nome=request.form['nome']
    categoria=request.form['categoria']
    console=request.form['console']
    jogo=Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect ('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario']
        return redirect ('/')
    else:
        flash('Login inválido')
        return redirect ('/login')

@app.route('/logout')
def logou():
    session['usuario_logado'] = None
    flash ('Seu logout foi efetuado com sucesso!')
    return redirect('/')


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)
