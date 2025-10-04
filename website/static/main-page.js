const only_steam_card_content = (params) => `
        <div class="game-image">
            <img src="${params.image_link}">
        </div>
        <div class="game-info">
            <div>
                <h2 class="game-title">${params.game_title}</h2>
                <div class="best-price">
                    <h2 class="price-value"><span class = "price-field">${params.price}</span> ₽</h2>
                    <p class="price-label">Только в стиме</p>
                </div>
                <p>Цена с комиссией: <span class="price-with-fee-field">${params.price_with_fee}</span> ₽</p>
            </div>
        </div>`;

const multiple_shops_card_content = (params) => `
        <div class="game-image">
            <img src="${params.image_link}">
        </div>
        <div class="game-info">
            <div>
                <h2 class="game-title">${params.game_title}</h2>
                <div class="best-price">
                    <h2 class="best-price-value"><span class = "best-price-field">${params.lowest_price}</span> ₽</h2>
                    <p class="price-label">Лучшая цена</p>

                </div>
            </div>

            <p class="shop-count">Все варианты: <span class = "shop-count-number">${params.amount_of_options}</span></p>
        </div> `;

let game_names;

fetch("/all-games-prices").then((res) => {
  games_prices = res.json().then((data) => {
    game_names = data;
    console.log(game_names);
    AddCards(game_names);
  });
});

async function AddCards(all_games_prices) {
  let game_grid = document.getElementById("game-grid");
  for (let game_data of all_games_prices) {
    console.log(game_data);
    await AddCard(game_data, game_grid);
  }
}

async function AddCard(game_data, game_card_grid) {
  let new_card;

  if (
    game_data.gabe_store_link == null &&
    game_data.zaka_zaka_link == null &&
    game_data.steam_pay_link == null
  ) {
    new_card = document.createElement("div");
    new_card.class = "game_card";
    new_card.innerHTML = only_steam_card_content({
        price: game_data.steam_price,
        price_with_fee: CalculatePriceWithFee(game_data.steam_price),
        image_link:game_data.image_link,
        game_title:game_data.name
    });

  } else {
    let prices = [];
    prices.push(parseFloat(game_data.steam_price));
    if (game_data.zaka_zaka_price != null) {
      prices.push(parseFloat(game_data.zaka_zaka_price));
    }
    if (game_data.steam_pay_price != null) {
      prices.push(parseFloat(game_data.steam_pay_price));
    }
    if (game_data.gabe_store_price != null) {
      prices.push(parseFloat(game_data.gabe_store_price));
    }
    console.log(prices);
    let lowest_price = Math.min(...prices);
    console.log(lowest_price);
    let amount_of_options = prices.length;
    console.log(amount_of_options);

    new_card = document.createElement("a");
    let card_inside = document.createElement("div");
    card_inside.className = "game-card";
    card_inside.innerHTML = multiple_shops_card_content({
        lowest_price:lowest_price.toString(),
        amount_of_options:amount_of_options,
        image_link:game_data.image_link,
        game_title:game_data.name,
    });
    new_card.appendChild(card_inside);
    new_card.href = "/" + game_data.id;
  }

  game_card_grid.appendChild(new_card);
}
