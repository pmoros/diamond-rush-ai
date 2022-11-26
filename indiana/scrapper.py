from time import sleep

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Scrapper():
    def __init__(self):
        profile = webdriver.FirefoxProfile()
        profile.accept_untrusted_certs = True
        self.driver = webdriver.Firefox()
        self.local_storage = LocalStorage(self.driver)

    def launch_game(self, target, max_level=20, wait_time=0.03):
        self.target = target
        self.wait_time = wait_time
        self.max_level = max_level
        self.canvas = None

        self.driver.get(self.target)
        self._set_local_storage()
        self._set_canvas()

    def read_map(self):
        element_png = self.canvas.screenshot_as_png
        return element_png

    def restart_level(self):
        self.driver.refresh()
        sleep(1)

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

    def close(self):
        self.driver.close()

    def _set_canvas(self):
        self.canvas = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//canvas"))
        )

    def _set_local_storage(self):
        self.local_storage.set("mp-diamond-rush-first_run", "0")
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
