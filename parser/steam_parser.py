from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service

from game import Game

amount_of_pages = 10

service = Service(executable_path='/usr/local/bin/geckodriver')
options = webdriver.FirefoxOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Firefox(options=options, service=service)
# driver = webdriver.Firefox()
def get_top_games_on_steam_with_special_prices() -> list[Game]:
    url = 'https://store.steampowered.com/specials/?flavor=contenthub_topsellers'
    driver.get(url)

    games_with_prices = list()
    try:
        WebDriverWait(driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//button[text()='Show more']")))
        for i in range(amount_of_pages):
            try:
                WebDriverWait(driver, 10).until(
                    expected_conditions.presence_of_element_located((By.XPATH, "//button[text()='Show more']")))
                WebDriverWait(driver, 10).until(
                    expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Show more']")))
                driver.find_element(By.XPATH, "//button[text()='Show more']").click()
                print("clicking 'Show more' button to get more games")
            except TimeoutException:
                break

        page_as_soup = BeautifulSoup(driver.page_source, 'html.parser')

        games_in_list = page_as_soup.find_all(class_="gASJ2lL_xmVNuZkWGvrWg")
        for game in games_in_list:
            game_as_soup = BeautifulSoup(str(game), 'html.parser')
            game_name = game_as_soup.find_all(class_='_2ekpT6PjwtcFaT4jLQehUK StoreSaleWidgetTitle')[0].text
            game_price = float(game_as_soup.find_all(class_='_3j4dI1yA7cRfCvK8h406OB')[0].text.split()[0].replace(",", "."))
            image_link = game_as_soup.find(class_='_2eQ4mkpf4IzUp1e9NnM2Wr')['src']
            print(image_link)
            games_with_prices.append(Game(game_name, game_price, image_link))

        return games_with_prices


    finally:
        driver.quit()
