from database.conexao import conectar

def recuperar_carrinho(usuario:str) -> list:
    conexao, cursor = conectar()
    cursor.execute("""
                  SELECT 
    CARRINHOS.COD_CARRINHO,
    USUARIOS.USUARIO,
    CARRINHOS.FINALIZADO,
    PRODUTOS.PRODUTO,
    ITENS_CARRINHOS.QUANTIDADE, 
    PRODUTOS.PRECO,
    PRODUTOS.FOTO
FROM CARRINHOS

INNER JOIN USUARIOS 
    ON USUARIOS.USUARIO = CARRINHOS.USUARIO 

INNER JOIN ITENS_CARRINHOS 
    ON CARRINHOS.COD_CARRINHO = ITENS_CARRINHOS.COD_CARRINHO

INNER JOIN PRODUTOS 
    ON PRODUTOS.CODIGO = ITENS_CARRINHOS.COD_PRODUTO

WHERE USUARIOS.USUARIO = 'aleatorio';
                    """)
    resultado = cursor.fetchall()
    conexao.close()
    return resultado

