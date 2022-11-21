from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Scrapper():
    def __init__(self, target, max_level=10, wait_time=0.03):
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        self.driver = webdriver.Firefox()
        self.local_storage = LocalStorage(self.driver)

        self.load(target, wait_time, max_level)

    def load(self, target, wait_time, max_level):
        self.target = target
        self.wait_time = wait_time
        self.max_level = max_level
        self.canvas = None

        self.driver.get(self.target)
        self._set_local_storage()

    def move_player(self, direction):
        sleep(0.5)
        action_chains = ActionChains(self.driver)
        if direction == "up":
            action_chains.key_down(Keys.ARROW_UP).pause(
                self.wait_time).perform()
            action_chains.key_up(Keys.ARROW_UP).perform()
        elif direction == "down":
            action_chains.key_down(Keys.ARROW_DOWN).pause(
                self.wait_time).perform()
            action_chains.key_up(Keys.ARROW_DOWN).perform()
        elif direction == "left":
            action_chains.key_down(Keys.ARROW_LEFT).pause(
                self.wait_time).perform()
            action_chains.key_up(Keys.ARROW_LEFT).perform()
        elif direction == "right":
            action_chains.key_down(Keys.ARROW_RIGHT).pause(
                self.wait_time).perform()
            action_chains.key_up(Keys.ARROW_RIGHT).perform()

    def save_game_map_auto(self, path_to_image):
        self.canvas = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//canvas"))
        )
        sleep(6)
        self.canvas.screenshot(path_to_image)
        return path_to_image

    def save_game_map(self, path_to_image):
        self.canvas = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//canvas"))
        )
        self.canvas.screenshot(path_to_image)
        return path_to_image

    def close(self):
        self.driver.close()

    def _set_local_storage(self):
        self.local_storage.set("mp-diamond-rush-first_run", 1)
        self.local_storage.set("isNewPlayer", "false")
        for i in range(1, self.max_level + 1):
            self.local_storage.set("Level {}".format(i), "passed")

        self.local_storage.set("levelToStart", "Level 1")


class LocalStorage:

    def __init__(self, driver):
        self.driver = driver

    def __len__(self):
        return self.driver.execute_script("return window.localStorage.length;")

    def items(self):
        return self.driver.execute_script(
            "var ls = window.localStorage, items = {}; "
            "for (var i = 0, k; i < ls.length; ++i) "
            "  items[k = ls.key(i)] = ls.getItem(k); "
            "return items; ")

    def keys(self):
        return self.driver.execute_script(
            "var ls = window.localStorage, keys = []; "
            "for (var i = 0; i < ls.length; ++i) "
            "  keys[i] = ls.key(i); "
            "return keys; ")

    def get(self, key):
        return self.driver.execute_script("return window.localStorage.getItem(arguments[0]);", key)

    def set(self, key, value):
        self.driver.execute_script(
            "window.localStorage.setItem(arguments[0], arguments[1]);", key, value)

    def has(self, key):
        return key in self.keys()

    def remove(self, key):
        self.driver.execute_script(
            "window.localStorage.removeItem(arguments[0]);", key)

    def clear(self):
        self.driver.execute_script("window.localStorage.clear();")

    def __getitem__(self, key):
        value = self.get(key)
        if value is None:
            raise KeyError(key)
        return value

    def __setitem__(self, key, value):
        self.set(key, value)

    def __contains__(self, key):
        return key in self.keys()

    def __iter__(self):
        return self.items().__iter__()

    def __repr__(self):
        return self.items().__str__()


def start():
    target = "https://www.minijuegosgratis.com/v3/games/games/prod/219431/diamond-rush/index.html?mp_api_as3_url=https%3A%2F%2Fssl.minijuegosgratis.com%2Flechuck%2Fas3%2Flatest.swf&mp_api_as3_url_bck=https%3A%2F%2Fapi.minijuegos.com%2Flechuck%2Fclient-as%2F&mp_api_id=1951&mp_api_js_url=https%3A%2F%2Fssl.minijuegosgratis.com%2Flechuck%2Fjs%2Flatest.js&mp_api_js_url_bck=https%3A%2F%2Fapi.minijuegos.com%2Flechuck%2Fclient-js%2F&mp_assets=https%3A%2F%2Fs2.minijuegosgratis.com%2F&mp_embed=0&mp_game_id=219431&mp_game_uid=diamond-rush&mp_game_url=https%3A%2F%2Fwww.minijuegos.com%2Fembed%2Fdiamond-rush&mp_int=1&mp_locale=es_ES&mp_player_type=IFRAME&mp_site_https_url=https%3A%2F%2Fwww.minijuegos.com%2F&mp_site_name=minijuegos.com&mp_site_url=https%3A%2F%2Fwww.minijuegos.com%2F&mp_timezone=America%2FBogota&mp_view_type=&mini_signature=cd6fbd6153154338558c881412712ab8&xdm_e=https%3A%2F%2Fwww.minijuegos.com&xdm_c=default9291&xdm_p=1"
    scrapper = Scrapper(target, max_level=5, wait_time=0.03)

    input("Press enter to stop game")

    scrapper.close()
