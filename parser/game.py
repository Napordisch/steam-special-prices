class Game:
    def __init__(self, name:str, steam_price, image_link:str):
        self.name = name
        self.steam_price = steam_price
        self.zaka_zaka_price = None
        self.gabe_store_price = None
        self.steam_pay_price = None
        self.steam_account_price = None
        self.image_link = image_link

        self.steam_link = None
        self.zaka_zaka_link = None
        self.gabe_store_link = None
        self.steam_pay_link = None
        self.steam_account_link = None
