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


def inserir_item(usuario, cod_produto, quantidade):
    conexao, cursor = conectar()

    
    cursor.execute("""
        SELECT COD_CARRINHO
        FROM Carrinhos
        WHERE USUARIO = %s
        AND FINALIZADO = 0
        LIMIT 1;
    """, [usuario])

    resultado_carrinho = cursor.fetchone()

    
    if resultado_carrinho:
        codigo_carrinho = resultado_carrinho["COD_CARRINHO"]

   
    else:
        cursor.execute("""
            INSERT INTO Carrinhos (USUARIO)
            VALUES (%s);
        """, [usuario])

        codigo_carrinho = cursor.lastrowid

    
    cursor.execute("""
        INSERT INTO Itens_Carrinhos
        (COD_CARRINHO, COD_PRODUTO, QUANTIDADE)
        VALUES (%s, %s, %s);
    """, [codigo_carrinho, cod_produto, quantidade])

    conexao.commit()
    conexao.close()

