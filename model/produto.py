from database.conexao import conectar

SELECT_BASE = "SELECT codigo, produto, descricao, destaque, preco, foto, disponibilidade FROM Produtos"

def recuperar():
    conexao, cursor = conectar()

    cursor.execute(SELECT_BASE)
    
  
    produtos = cursor.fetchall()
    
    conexao.close()
    return produtos

def rec_destaq():
    conexao, cursor = conectar()

   
    query = f"{SELECT_BASE} WHERE destaque = %s"
    cursor.execute(query, [True])

    produtos = cursor.fetchall()
    conexao.close()
    return produtos

def rec_produto(codigo: int):  
    conexao, cursor = conectar()
    
    query = f"{SELECT_BASE} WHERE codigo = %s"
    cursor.execute(query, [codigo])


    produto = cursor.fetchone()
    
    conexao.close()
    return produto