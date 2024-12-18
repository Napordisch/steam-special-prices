const only_steam_card_content =`
        <div class="game-image">
            <img src="">
        </div>
        <div class="game-info">
            <div>
                <h2 class="game-title"></h2>
                <div class="best-price">
                    <h2 class="price-value"><span class = "price-field"></span> ₽</h2>
                    <p class="price-label">Только в стиме</p>
                </div>
                <p>Цена с комиссией: <span class="price-with-fee-field"></span> ₽</p>
            </div>
        </div>`

const multiple_shops_card_content = `
        <div class="game-image">
            <img src="">
        </div>
        <div class="game-info">
            <div>
                <h2 class="game-title"></h2>
                <div class="best-price">
                    <h2 class="best-price-value"><span class = "best-price-field"></span> ₽</h2>
                    <p class="price-label">Лучшая цена</p>

                </div>
            </div>

            <p class="shop-count">Все варианты: <span class = "shop-count-number"></span></p>
        </div> `



let game_names;

fetch('/all-game-names').then(res => {
    game_names=res.json().then(data => {
        game_names = data;
        console.log(game_names);
        AddCards(game_names).catch(err => console.error(err));
    });
})

async function AddCards(game_names) {
    let game_grid = document.getElementById("game-grid");
    for (let game_name of game_names) {
        console.log(game_name);
        await AddCard(game_name, game_grid).catch(err => console.error(err));
    }
}

async function AddCard(game_name, game_card_grid) {
    await fetch('/game-info/' + game_name).then(res => {
        let new_card;
        res.json().then(game_data => {
            if (game_data.gabe_store_link == null &&
            game_data.zaka_zaka_link == null &&
            game_data.steam_pay_link == null) {
                new_card = document.createElement("div");
                new_card.class = "game_card";
                new_card.innerHTML = only_steam_card_content;
                new_card.getElementsByClassName("price-field")[0].innerHTML = game_data.steam_price;
                console.log(game_data);
                new_card.getElementsByClassName("price-with-fee-field")[0].innerHTML = CalculatePriceWithFee(game_data.steam_price);
            } else {
                let prices = [];
                prices.push(parseFloat(game_data.steam_price));
                if (game_data.zaka_zaka_price != null) {prices.push(parseFloat(game_data.zaka_zaka_price));}
                if (game_data.steam_pay_price != null) {prices.push(parseFloat(game_data.steam_pay_price));}
                if (game_data.gabe_store_price != null) {prices.push(parseFloat(game_data.gabe_store_price));}
                console.log(prices);
                let lowest_price = Math.min(...prices);
                console.log(lowest_price);
                let amount_of_options = prices.length
                console.log(amount_of_options);

                new_card = document.createElement("a");
                let card_inside = document.createElement("div")
                card_inside.className="game-card"
                card_inside.innerHTML=multiple_shops_card_content;
                new_card.appendChild(card_inside);
                new_card.href = "/" + game_data.id;
                new_card.getElementsByClassName("best-price-field")[0].innerHTML = lowest_price.toString();
                new_card.getElementsByClassName("shop-count-number")[0].innerHTML = amount_of_options;
            }
            new_card.querySelector("img").src = game_data.image_link;
            new_card.getElementsByClassName("game-title")[0].innerHTML = game_data.name;
            game_card_grid.appendChild(new_card);
        })
    }).catch(err => {console.error(err)})
}


function CalculatePriceWithFee(price) {
    let price_value = parseFloat(price);
    return (price_value + (price_value * 0.14)).toString();
}