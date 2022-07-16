from flask import Flask, render_template, flash, redirect, json, request

app = Flask(__name__)
app.config['SECRET_KEY'] = "@my-replit-secret"

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/sobre')
def sobre():
  return render_template('sobre.html')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/obrigado')
def obrigado():
    return render_template('obrigado.html')

@app.route('/envio', methods=['GET', 'POST']) 
def envio():
    return render_template('envio.html') 

@app.route('/switch', defaults={"desconto": "0"})
@app.route('/switch/<desconto>')
def switch(desconto):
  if(desconto == "pix"):
    return render_template('switch.html', promocao=True, desconto=20)
  else:
    return render_template('switch.html', promocao=False, desconto=0)

@app.route('/procontrole', defaults={"desconto": "0"})
@app.route('/procontrole/<desconto>')
def procontrole(desconto):
  if(desconto == "pix"):
    return render_template('procontrole.html', promocao=True, desconto=20)
  else:
    return render_template('procontrole.html', promocao=False, desconto=0)

@app.route('/avaliacoes')
def avaliacoes():
  clientes = [ {"nome": "Alana", "nota": 5, "comentario": "Loja muito boa, produto chegou muito rápido na minha casa!"},
              {"nome": "Pedro", "nota": 3, "comentario": "Produto muito bom, mas a loja demorou a postar meu produto, por isso dou 3 estrelas"},
              {"nome": "Alice", "nota": 5, "comentario": "Excelente!"},
              {"nome": "Bia", "nota": 4, "comentario": "Bom console, mas os jogos são caros"},
              {"nome": "Paulo Sérgio", "nota": 5, "comentario": "Gostei muito!"},
              {"nome": "Mário Mário", "nota": 2, "comentario": "Meu switch veio com defeito, acionei a garantia!"},
             ]
  return render_template('avaliacoes.html', clientes=clientes)

app.run(host='0.0.0.0', port=81)