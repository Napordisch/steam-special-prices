import mysql.connector
from mysql.connector import Error
import time

class DataBase:
    def create_table(self):
        table_creation = '''
        CREATE TABLE IF NOT EXISTS game_prices (
            name VARCHAR(255) UNIQUE,
            steam_price DECIMAL(10, 2),
            zaka_zaka_price DECIMAL(10, 2),
            steam_pay_price DECIMAL(10, 2),
            steam_account_price DECIMAL(10, 2),
            gabe_store_price DECIMAL(10, 2),
            ggsell_price DECIMAL(10, 2)
        );
        '''
        self.push(table_creation)

    def __init__(self, host, user:str, password, database_name, port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database_name
        self.port = port
        self.create_table()

    def push(self, query):
        connection_attempts = 0
        while connection_attempts < 10:
            connection_attempts += 1
            try:
                connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database
                )
                if connection.is_connected():
                    cursor = connection.cursor()
                    cursor.execute(query)
                    connection.commit()
                    cursor.close()
                    connection.close()
                    break

            except Error as e:
                time.sleep(5)
                continue



    def update_game_prices(self, game):
        fields_available = 'name, steam_price'
        fields = f'"{game.name}", {game.steam_price}'
        if game.zaka_zaka_price is not None:
            fields_available += ', zaka_zaka_price'
            fields += f', {game.zaka_zaka_price}'
        if game.steam_pay_price is not None:
            fields_available += ', steam_pay_price'
            fields += f', {game.steam_pay_price}'
        if game.steam_account_price is not None:
            fields_available += ', steam_account_price'
            fields += f', {game.steam_account_price}'
        if game.gabe_store_price is not None:
            fields_available += ', gabe_store_price'
            fields += f', {game.gabe_store_price}'
        if game.ggsell_price is not None:
            fields_available += ', ggsell_price'
            fields += f', {game.ggsell_price}'

        update_game_query = f'''
        INSERT INTO game_prices ({fields_available}) VALUES ({fields})
        ON DUPLICATE KEY UPDATE
            steam_price = VALUES(steam_price),
            zaka_zaka_price = VALUES(zaka_zaka_price),
            steam_pay_price = VALUES(steam_pay_price),
            steam_account_price = VALUES(steam_account_price),
            gabe_store_price = VALUES(gabe_store_price),
            ggsell_price = VALUES(ggsell_price);
        '''
        self.push(update_game_query)


if __name__ == "__main__":
    data_base = DataBase('db', 'user', 'user_password', 'game_prices')
