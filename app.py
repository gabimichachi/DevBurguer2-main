from flask import Flask, render_template, redirect
from model.produto import recuperar
from model.produto import rec_destaq
from model.produto import rec_produto


app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    produtos = recuperar()
    destaques = rec_destaq()
    return render_template("index.html", produtos = produtos, destaques = destaques)

@app.route("/produto/<codigo>")
def pagina_produto(codigo):
    produto = rec_produto(codigo)
   
    return render_template("produto.html", produto = produto)

app.run(debug=True)