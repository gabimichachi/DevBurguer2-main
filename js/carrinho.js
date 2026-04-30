async function mostrar_carrinho() {
    try {
        const resposta = await fetch("/api/get/carrinho");

        if (!resposta.ok) {
            alert("ERRO AO CARREGAR CARRINHO!");
            return;
        }

        const dados = await resposta.json();
        const carrinhoContainer = document.getElementById("carrinho");
        carrinhoContainer.innerHTML = "";

        let total = 0;

        for (let dado of dados) {
            total += dado.preco;

            let linha = `
                <div class="cart-item">
                    <img src="${dado.imagem}" alt="${dado.nome}" class="cart-item__image">
                    <div class="cart-item__info">
                        <div class="cart-item__top">
                            <h3 class="cart-item__name">${dado.nome}</h3>
                            <button class="remove-item-btn" title="remover item">🗑</button>
                        </div>
                        <div class="cart-item__bottom">
                            <span class="cart-item__price">R$ ${dado.preco.toFixed(2)}</span>
                        </div>
                    </div>
                </div>
            `;
            carrinhoContainer.innerHTML += linha;
        }

    } catch (erro) {
        console.error(erro);
        alert("Erro de rede ao carregar o carrinho.");
    }
}