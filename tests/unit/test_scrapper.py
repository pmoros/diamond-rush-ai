from unittest import TestCase

from indiana.scrapper import scrapper


class TestScrapper(TestCase):
    def setUp(self):
        self.target = "https://www.minijuegosgratis.com/v3/games/games/prod/219431/diamond-rush/index.html?mp_api_as3_url=https%3A%2F%2Fssl.minijuegosgratis.com%2Flechuck%2Fas3%2Flatest.swf&mp_api_as3_url_bck=https%3A%2F%2Fapi.minijuegos.com%2Flechuck%2Fclient-as%2F&mp_api_id=1951&mp_api_js_url=https%3A%2F%2Fssl.minijuegosgratis.com%2Flechuck%2Fjs%2Flatest.js&mp_api_js_url_bck=https%3A%2F%2Fapi.minijuegos.com%2Flechuck%2Fclient-js%2F&mp_assets=https%3A%2F%2Fs2.minijuegosgratis.com%2F&mp_embed=0&mp_game_id=219431&mp_game_uid=diamond-rush&mp_game_url=https%3A%2F%2Fwww.minijuegos.com%2Fembed%2Fdiamond-rush&mp_int=1&mp_locale=es_ES&mp_player_type=IFRAME&mp_site_https_url=https%3A%2F%2Fwww.minijuegos.com%2F&mp_site_name=minijuegos.com&mp_site_url=https%3A%2F%2Fwww.minijuegos.com%2F&mp_timezone=America%2FBogota&mp_view_type=&mini_signature=cd6fbd6153154338558c881412712ab8&xdm_e=https%3A%2F%2Fwww.minijuegos.com&xdm_c=default9291&xdm_p=1"
        self.scrapper = scrapper.Scrapper(self.target)
        self.path_to_image = "resources/current_game.png"

    def test_load(self):
        self.assertEqual(self.scrapper.driver.current_url, self.target)

    def test_get_game_map(self):
        # * This can be tested by mocking the input function
        self.scrapper.save_game_map_auto(self.path_to_image)

    def tearDown(self):
        self.scrapper.close()
