function mostrar_carrinho()
{
    const resposta = fetch("http://10.110.134.2:8080/api/get/carrinho")

    if (resposta.ok) {
        alert("ERRO AO CARREGAR CARRINHO!")

    }else{
        const carrinho = document.getElementById("carrinho")

        carrinho.innerHTML = "";

        let total = 0;

        for (let dado of dados) {
            total = total + dado.preco

            let linha = `
                        teste
                        <img src = "${dado.imagem}" alt = "hambúrguer" class= "cart-item__image">

                        <div class= "cart-item__info>

                        <!-- TOPO (nome + remover) -->
                        <div class = "class-item__top">
                            <h3 class = "cart-item__name" >${dado.nome}</h3>
                            <button class = "remove-item-btn" title = "remover item">🗑</button>
                        </div>

                        <! -- PARTE DE BAIXO -->
                        <div class = "cart-item__button">
                            <span class = "cart-item__price">R$ ${dado.preco}</span>
                        </div>
                        </div>
                        `
            carrinho.innerHTML += linha
        }
    }
}