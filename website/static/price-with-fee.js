function CalculatePriceWithFee(price) {
  let price_value = parseFloat(price);
  return (price_value + price_value * 0.14).toFixed(2);
}