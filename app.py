from flask import Flask, jsonify, render_template, redirect, request, session
from model import usuario
from model.carrinho import recuperar_carrinho
from model.produto import recuperar, rec_destaq, rec_produto
from model.usuario import Usuario

app = Flask(__name__)

app.secret_key = "chave_secreta_muito_segura_aqui"

@app.route("/")
def pagina_inicial():
    produtos = recuperar()
    destaques = rec_destaq()
    
    usuario_logado = session.get("nome")
    return render_template("index.html", 
                           produtos=produtos, 
                           destaques=destaques, 
                           usuario=usuario_logado)

@app.route("/produto/<codigo>")
def pagina_produto(codigo):
    produto = rec_produto(codigo)
    if not produto:
        return "Produto não encontrado", 404
    return render_template("produto.html", produto=produto)

@app.route("/cadastrar_usuario", methods=["POST"])
def cadastrar_usuario():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")
    nome = request.form.get("nome")
    
    if usuario and senha and nome:
        novo_usuario = Usuario(usuario, senha, nome)
        novo_usuario.cadastrar()
    
    return redirect("/cadastro-login") 

@app.route("/logar/usuario", methods=["POST"])
def logar_usuario():
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    resultado = Usuario.logar(usuario, senha)

    if resultado:
        session["usuario_logado"] = resultado
        session["nome"] = resultado
        return redirect("/")
    else:
        return redirect("/cadastro-login")

@app.route("/logout")
def logout():
    session.clear() 
    return redirect("/")

@app.get("/cadastro-login")
def cadastro_login():
    return render_template("cadastro_login.html")


@app.route("/api/get/carrinho", methods = ["GET"])
def api_get_carrinho():
    if "usuario_logado" in session:
     usuario = session["usuario_logado"]
     carrinho = recuperar_carrinho(usuario)
     return jsonify(carrinho), 200
    else:
        return jsonify({"message":"usuario não logado"})




if __name__ == "__main__":
    app.run(debug=True)