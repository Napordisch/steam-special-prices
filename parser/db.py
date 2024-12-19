import time
from datetime import datetime, timezone

import mysql.connector
from mysql.connector import Error

import utilities
from game import Game


class DataBase:
    def create_tables(self):
        prices_table_creation = '''
        CREATE TABLE IF NOT EXISTS game_prices (
            id VARCHAR(512) PRIMARY KEY,
            steam_price DECIMAL(10, 2),
            zaka_zaka_price DECIMAL(10, 2),
            steam_pay_price DECIMAL(10, 2),
            steam_account_price DECIMAL(10, 2),
            gabe_store_price DECIMAL(10, 2),
            place_in_top INTEGER,
            update_time DATETIME
        );
        '''
        self.push(prices_table_creation)

        images_table_creation = '''
        CREATE TABLE IF NOT EXISTS game_images (
            id VARCHAR(512) PRIMARY KEY,
            image_link TEXT
        );
        '''
        self.push(images_table_creation)

        names_table_creation = '''
        CREATE TABLE IF NOT EXISTS game_names (
            id VARCHAR(512) PRIMARY KEY,
            name TEXT
        );
        '''
        self.push(names_table_creation)

        links_table_creation = '''
        CREATE TABLE IF NOT EXISTS game_links (
            id VARCHAR(512) PRIMARY KEY,
            steam_link TEXT,
            zaka_zaka_link TEXT,
            steam_pay_link TEXT,
            steam_account_link TEXT,
            gabe_store_link TEXT
        );
        '''
        self.push(links_table_creation)

    def __init__(self, host, user: str, password, database_name, port=3306):
        self.host = host
        self.user = user
        self.password = password
        self.database = database_name
        self.port = port
        self.create_tables()

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
                print(e)
                time.sleep(5)
                continue

    def update_game_prices(self, game: Game, place_in_top):
        update_time = datetime.now(timezone.utc)
        fields_available = 'id, steam_price, place_in_top, update_time'
        fields = f'"{utilities.to_kebab_case(game.name)}", {game.steam_price}, {place_in_top}, "{update_time}"'
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

        update_game_query = f'''
        INSERT INTO game_prices ({fields_available})
        VALUES ({fields})
        ON DUPLICATE KEY UPDATE
            steam_price = VALUES(steam_price),
            zaka_zaka_price = VALUES(zaka_zaka_price),
            steam_pay_price = VALUES(steam_pay_price),
            steam_account_price = VALUES(steam_account_price),
            gabe_store_price = VALUES(gabe_store_price),
            update_time = VALUES(update_time);
        '''
        self.push(update_game_query)

    def add_game_image(self, game: Game):
        add_image_query = f'''
        INSERT INTO game_images (id, image_link)
        VALUES ("{utilities.to_kebab_case(game.name)}", "{game.image_link}")
        ON DUPLICATE KEY UPDATE
            image_link = VALUES(image_link);
        '''
        self.push(add_image_query)

    def add_game_name(self, game: Game):
        add_name_query = f'''
        INSERT INTO game_names (id, name)
        VALUES ("{utilities.to_kebab_case(game.name)}", "{game.name}")
        ON DUPLICATE KEY UPDATE
            name = VALUES(name);
        '''
        self.push(add_name_query)

    def add_game_links(self, game: Game):
        fields_available = 'id'
        fields = f'"{utilities.to_kebab_case(game.name)}"'
        if game.zaka_zaka_link is not None:
            fields_available += ', zaka_zaka_link'
            fields += f', "{game.zaka_zaka_link}"'
        if game.steam_pay_link is not None:
            fields_available += ', steam_pay_link'
            fields += f', "{game.steam_pay_link}"'
        if game.steam_account_link is not None:
            fields_available += ', steam_account_link'
            fields += f', "{game.steam_account_link}"'
        if game.gabe_store_link is not None:
            fields_available += ', gabe_store_link'
            fields += f', "{game.gabe_store_link}"'
        add_links_query = f'''
                INSERT INTO game_links ({fields_available})
                VALUES ({fields})
                ON DUPLICATE KEY UPDATE
                    zaka_zaka_link = VALUES(zaka_zaka_link),
                    steam_pay_link = VALUES(steam_pay_link),
                    steam_account_link = VALUES(steam_account_link),
                    gabe_store_link = VALUES(gabe_store_link);
                '''
        self.push(add_links_query)


if __name__ == "__main__":
    data_base = DataBase('db', 'user', 'user_password', 'game_info')
