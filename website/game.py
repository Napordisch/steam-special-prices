class Game:
    def __init__(self, data_as_dict):
        self.id = data_as_dict['id']
        self.name = data_as_dict['name']
        self.steam_price = data_as_dict['steam_price']
        self.zaka_zaka_price = data_as_dict['zaka_zaka_price']
        self.gabe_store_price = data_as_dict['gabe_store_price']
        self.steam_pay_price = data_as_dict['steam_pay_price']
        self.steam_account_price = data_as_dict['steam_account_price']
        self.image_link = data_as_dict['image_link']

        # self.steam_link = data_as_dict['steam_link']
        self.zaka_zaka_link = data_as_dict['zaka_zaka_link']
        self.gabe_store_link = data_as_dict['gabe_store_link']
        self.steam_pay_link = data_as_dict['steam_pay_link']
        # self.steam_account_link = data_as_dict['steam_account_link']
    
    def only_steam_info(self):
        return self.zaka_zaka_price == None and self.gabe_store_price == None and self.steam_pay_price == None and self.steam_account_price == None

    def existing_prices(self):
        return [price for price in [self.steam_price, self.zaka_zaka_price, self.gabe_store_price, self.steam_pay_price, self.steam_account_price] if price != None]

    def amount_of_prices(self):
        return len(self.existing_prices())
        

    def lowest_price(self):
        prices = self.existing_prices()
        return min(prices)

    def price_with_fee(self):
        price = float(self.steam_price)
        return price + price * 0.3

