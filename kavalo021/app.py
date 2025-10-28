
## IMPORTANDO "PARTES" DO FLASK
from flask import Flask, render_template,request

app = Flask(__name__)


nome = "imune ao conhecimento"

### Criando Rotas

## / Significa principal onde o site já vai de cara

@app.route("/")
def ola():
    return f"Olá {nome}"

@app.route("/tchau")
def tchau():
    return f"tchau {nome}"

@app.route("/adeus")
def adeus():
    return f"adeus faltem no dia da prova 👌😊👍"

## Aqui vamos criar uma nova rota, dessa vez vai ser a /contato

@app.route("/contato")
def contato():
    return render_template('contato.html')


## Sua vez crie uma nova rota dessa vez /hobbies, la coloque algo que você goste de fazer, exemplo : Jogar bola

# lembre- se de criar um template chamado hobbies.html
@app.route("/hobbies")
def hobbies():
    meus_hobbies = ['Jogar Bola', 'Dançar', 'Pescar','Programar']
    return render_template('hobbies.html', hobbies = meus_hobbies)

## Executando o arquivo 
if __name__ == '__main__':
    app.run(debug=True)


