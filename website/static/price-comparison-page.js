const otherShopRow = (shopLink, shopName, shopPrice) => `
        <td><a href="${shopLink}" class="shop-link-with-name">${shopName}</a></td>
        <td><span class="price-value">${shopPrice}</span> ₽</td>
`;



const currentURL = window.location.href;
const currentGameId = currentURL.substring(currentURL.lastIndexOf("/") + 1);

fetch("/game-info/" + currentGameId).then((res) => {
  res.json().then((game) => {
    console.log(game);
    fillPage(game);
  });
});

function fillPage(gameInfo) {
  document.querySelector("img").src = gameInfo.image_link;
  document.getElementsByClassName("price-without-fee-value")[0].innerHTML =
    gameInfo.steam_price;
  document.getElementsByClassName("price-with-fee-value")[0].innerHTML =
    CalculatePriceWithFee(gameInfo.steam_price);
  if (gameInfo.zaka_zaka_price != null)
    addShopRow(gameInfo.zaka_zaka_link, "Zaka Zaka", gameInfo.zaka_zaka_price);
  if (gameInfo.steam_pay_price != null)
    addShopRow(gameInfo.steam_pay_link, "Steampay", gameInfo.steam_pay_price);
  if (gameInfo.gabe_store_price != null)
    addShopRow(
      gameInfo.gabe_store_link,
      "Gabestore",
      gameInfo.gabe_store_price
    );
}

function addShopRow(shopLink, shopName, shopPrice) {
  let newRow = document.createElement("tr");
  newRow.className = "other-shop-row";
  newRow.innerHTML = otherShopRow(shopLink, shopName,shopPrice);
  document.querySelector("table").appendChild(newRow);
}