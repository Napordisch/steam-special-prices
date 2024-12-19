const otherShopRow = `
    <td><a href="" class="shop-link-with-name"></a></td>
    <td><span class="price-value"></span> ₽</td>
`

const currentURL = window.location.href;
const currentGameId = currentURL.substring(currentURL.lastIndexOf('/') + 1);

fetch('/game-info/' + currentGameId).then(res => {
    res.json().then(game => {
        console.log(game);
        fillPage(game);
    })
})

function fillPage(gameInfo) {
    document.querySelector("img").src = gameInfo.image_link;
    document.getElementsByClassName("price-without-fee-value")[0].innerHTML = gameInfo.steam_price;
    document.getElementsByClassName("price-with-fee-value")[0].innerHTML = CalculatePriceWithFee(gameInfo.steam_price);
    if (gameInfo.zaka_zaka_price != null) addShopRow(gameInfo.zaka_zaka_link, "Zaka Zaka", gameInfo.zaka_zaka_price);
    if (gameInfo.steam_pay_price != null) addShopRow(gameInfo.steam_pay_link, "Steampay", gameInfo.steam_pay_price);
    if (gameInfo.gabe_store_price != null) addShopRow(gameInfo.gabe_store_link, "Gabestore", gameInfo.gabe_store_price);

}


function CalculatePriceWithFee(price) {
    let price_value = parseFloat(price);
    return (price_value + (price_value * 0.14)).toFixed(2);
}


function addShopRow(shopLink, shopName, shopPrice) {
    let newRow = document.createElement("tr");
    newRow.className = "other-shop-row";
    newRow.innerHTML = otherShopRow;
    linkElement = newRow.getElementsByClassName("shop-link-with-name")[0];
    linkElement.href = shopLink;
    linkElement.innerHTML = shopName;
    newRow.getElementsByClassName("price-value")[0].innerHTML = shopPrice;
    document.querySelector("table").appendChild(newRow);
}