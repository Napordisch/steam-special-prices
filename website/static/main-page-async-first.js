async function AddCard(only_steam_card, multiple_shop_game_card, game_name){
    try {
        const game_info_response = await fetch('/game-info/' + game_name);
        const game_info = await game_info_response.json();
        let new_card;
        if (game_info["steam_pay_price"] == null && game_info["zaka_zaka_price"] == null && game_info["gabe_store_price"] == null){
            new_card = only_steam_card;
            new_card = new_card.getElementsByClassName("game-card")[0];
        } else {
            new_card = multiple_shop_game_card;
            new_card = new_card.querySelector("a");
        }
        new_card.querySelector("img").setAttribute("src", game_info["image_link"]);
        console.log(new_card);
        document.getElementById('game-grid').appendChild(new_card);
    }
    catch (error) {console.error(error)}
}

async function fillPage() {
    let parser = new DOMParser();
    try {
        let multiple_shops_card_response;
        let only_steam_card_response;
        let game_names_response;
        [only_steam_card_response, multiple_shops_card_response, game_names_response] = await Promise.all([
            fetch ('static/page-parts/only_steam_game.html'),
            fetch('static/page-parts/game_card_with_other_shops.html'),
            fetch('/all-game-names')
        ]);
        const only_steam_card = await only_steam_card_response.text();
        const only_steam_card_document = parser.parseFromString(only_steam_card, 'text/html')
        const multiple_shops_card = await multiple_shops_card_response.text();
        const multiple_shops_card_document = parser.parseFromString(multiple_shops_card, 'text/html')
        const game_names = await game_names_response.json();
        console.log(only_steam_card);
        console.log(multiple_shops_card);
        console.log(game_names);
        for (const game_name of game_names) {
            await AddCard(only_steam_card_document, multiple_shops_card_document, game_name);
        }
    }
    catch (error) {console.error(error)}
}
fillPage().catch(error => console.log(error));