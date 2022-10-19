from time import sleep

import elements.processor as processor
from scrapper.scrapper import Scrapper

target = "https://www.minijuegosgratis.com/v3/games/games/prod/219431/diamond-rush/index.html?mp_api_as3_url=https%3A%2F%2Fssl.minijuegosgratis.com%2Flechuck%2Fas3%2Flatest.swf&mp_api_as3_url_bck=https%3A%2F%2Fapi.minijuegos.com%2Flechuck%2Fclient-as%2F&mp_api_id=1951&mp_api_js_url=https%3A%2F%2Fssl.minijuegosgratis.com%2Flechuck%2Fjs%2Flatest.js&mp_api_js_url_bck=https%3A%2F%2Fapi.minijuegos.com%2Flechuck%2Fclient-js%2F&mp_assets=https%3A%2F%2Fs2.minijuegosgratis.com%2F&mp_embed=0&mp_game_id=219431&mp_game_uid=diamond-rush&mp_game_url=https%3A%2F%2Fwww.minijuegos.com%2Fembed%2Fdiamond-rush&mp_int=1&mp_locale=es_ES&mp_player_type=IFRAME&mp_site_https_url=https%3A%2F%2Fwww.minijuegos.com%2F&mp_site_name=minijuegos.com&mp_site_url=https%3A%2F%2Fwww.minijuegos.com%2F&mp_timezone=America%2FBogota&mp_view_type=&mini_signature=cd6fbd6153154338558c881412712ab8&xdm_e=https%3A%2F%2Fwww.minijuegos.com&xdm_c=default9291&xdm_p=1"
path_to_image = "resources/current_game.png"

scrapper = Scrapper(target)


if __name__ == '__main__':
    scrapper.save_game_map_auto(path_to_image)
    # game_map = processor.get_game_map(path_to_image)

    sample_moves = ["right", "right", "right",
                    "right", "right", "down", "down", "down", "left", "left", "left", "left", "left", "down", "down", "right", "down", "right", "right", "right", "right", "down"]

    for move in sample_moves:
        scrapper.move_player(move)

    sleep(1)

    scrapper.close()
