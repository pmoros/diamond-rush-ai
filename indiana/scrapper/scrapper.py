from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Scrapper():
    def __init__(self, target):
        self.target = target
        self.driver = webdriver.Firefox()
        self.local_storage = LocalStorage(self.driver)
        self.driver.get(self.target)
        self.canvas = None
        self.load()

    def load(self):
        self.max_level = 5
        self.driver.get(self.target)

    def move_player(self, direction):
        if direction == "up":
            pass
        elif direction == "down":
            pass
        elif direction == "left":
            pass
        elif direction == "right":
            # keyboard.press_and_release("right")
            ActionChains(self.driver).key_down(Keys.ARROW_RIGHT).pause(
                0.2).key_up(Keys.ARROW_RIGHT).perform()

    def save_game_map_auto(self, path_to_image):
        # Sets the levels to passed
        self._set_local_storage()
        self.canvas = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//canvas"))
        )
        sleep(2)
        self.canvas.screenshot(path_to_image)
        return path_to_image

    def save_game_map(self, path_to_image):
        # Sets the levels to passed
        self._set_local_storage()
        # Ask the user to start the game
        input("Press Enter to start the game...")
        sleep(5)
        self.canvas = WebDriverWait(self.driver, 10).until(
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
