import numpy as np

from classifier import Item


class ClassifierUtility():

    def __init__(self):
        pass

    def get_matrix(self, level):
        if level == "1":
            matrix = [
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value],
                [Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value],
                [Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value],
                [Item.WALL.value, Item.FLOOR.value, Item.INDIANA.value, Item.DIAMOND.value, Item.DIAMOND.value,
                    Item.DIAMOND.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value],
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.DIAMOND.value, Item.FLOOR.value, Item.WALL.value],
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.DIAMOND.value, Item.FLOOR.value, Item.WALL.value],
                [Item.WALL.value, Item.FLOOR.value, Item.DIAMOND.value, Item.FLOOR.value, Item.DIAMOND.value,
                    Item.DIAMOND.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value],
                [Item.WALL.value, Item.FLOOR.value, Item.DIAMOND.value, Item.FLOOR.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value],
                [Item.WALL.value, Item.FLOOR.value, Item.DIAMOND.value, Item.FLOOR.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value],
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.FLOOR.value, Item.DIAMOND.value,
                    Item.DIAMOND.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value],
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value,
                    Item.WALL.value, Item.FLOOR.value, Item.EXIT.value, Item.FLOOR.value, Item.WALL.value],
                [Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value,
                    Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value],
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value]
            ]

        elif level == "2":
            matrix = [
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value],
                [Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value, Item.DIAMOND.value, Item.FLOOR.value,
                    Item.FLOOR.value, Item.WALL.value, Item.LAVA.value, Item.LAVA.value, Item.WALL.value],
                [Item.WALL.value, Item.FLOOR.value, Item.DIAMOND.value, Item.FLOOR.value, Item.DIAMOND.value, Item.FLOOR.value,
                    Item.WALL.value, Item.LAVA.value, Item.LAVA.value, Item.WALL.value],
                [Item.WALL.value, Item.PYKE_DOWN.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.FLOOR.value, Item.WALL.value, Item.WALL.value, Item.FLOOR.value, Item.WALL.value],
                [Item.WALL.value, Item.DIAMOND.value, Item.LAVA.value, Item.LAVA.value, Item.WALL.value,
                    Item.DIAMOND.value, Item.FLOOR.value, Item.DIAMOND.value, Item.FLOOR.value, Item.WALL.value],
                [Item.WALL.value, Item.DIAMOND.value, Item.LAVA.value, Item.LAVA.value, Item.WALL.value,
                    Item.DIAMOND.value, Item.FLOOR.value, Item.DIAMOND.value, Item.FLOOR.value, Item.WALL.value],
                [Item.WALL.value, Item.FLOOR.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.PYKE_DOWN.value, Item.WALL.value, Item.LAVA.value, Item.LAVA.value, Item.WALL.value],
                [Item.WALL.value, Item.FLOOR.value, Item.WALL.value, Item.FLOOR.value, Item.DIAMOND.value,
                    Item.PYKE_DOWN.value, Item.WALL.value, Item.LAVA.value, Item.LAVA.value, Item.WALL.value],
                [Item.WALL.value, Item.FLOOR.value, Item.WALL.value, Item.EXIT.value, Item.WALL.value,
                    Item.PYKE_DOWN.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value],
                [Item.WALL.value, Item.FLOOR.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value],
                [Item.WALL.value, Item.DIAMOND.value, Item.DIAMOND.value, Item.PYKE_DOWN.value, Item.PYKE_DOWN.value,
                    Item.FLOOR.value, Item.FLOOR.value, Item.INDIANA.value, Item.FLOOR.value, Item.WALL.value],
                [Item.WALL.value, Item.DIAMOND.value, Item.DIAMOND.value, Item.WALL.value, Item.WALL.value,
                    Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value],
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value]
            ]

        elif level == "3":
            matrix = [
                # row 0
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value],
                # row 1
                [Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value,
                    Item.FLOOR.value, Item.WALL.value, Item.FLOOR.value, Item.DIAMOND.value, Item.WALL.value],
                # row 2
                [Item.WALL.value, Item.INDIANA.value, Item.FLOOR.value, Item.WALL.value, Item.WALL.value, Item.FLOOR.value,
                    Item.KEY_DOOR_CLOSED.value, Item.FLOOR.value, Item.EXIT.value, Item.WALL.value],
                # row 3
                [Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value, Item.PYKE_DOWN.value, Item.FLOOR.value,
                    Item.FLOOR.value, Item.WALL.value, Item.FLOOR.value, Item.DIAMOND.value, Item.WALL.value],
                # row 4
                [Item.WALL.value, Item.WALL.value, Item.PYKE_DOWN.value, Item.WALL.value, Item.KEY_DOOR_CLOSED.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value],
                # row 5
                [Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value, Item.FLOOR.value,
                    Item.FLOOR.value, Item.WALL.value, Item.DIAMOND.value, Item.DIAMOND.value, Item.WALL.value],
                # row 6
                [Item.WALL.value, Item.FLOOR.value, Item.DIAMOND.value, Item.WALL.value, Item.FLOOR.value,
                    Item.FLOOR.value, Item.KEY_DOOR_CLOSED.value, Item.KEY.value, Item.DIAMOND.value, Item.WALL.value],
                # row 7
                [Item.WALL.value, Item.WALL.value, Item.FLOOR.value, Item.WALL.value, Item.FLOOR.value,
                    Item.FLOOR.value, Item.WALL.value, Item.DIAMOND.value, Item.DIAMOND.value, Item.WALL.value],
                # row 8
                [Item.WALL.value, Item.KEY.value, Item.FLOOR.value, Item.WALL.value, Item.DIAMOND.value,
                    Item.FLOOR.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value],
                # row 9
                [Item.WALL.value, Item.FLOOR.value, Item.WALL.value, Item.WALL.value, Item.FLOOR.value,
                    Item.FLOOR.value, Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value],
                # row 10
                [Item.WALL.value, Item.DIAMOND.value, Item.PYKE_DOWN.value, Item.PYKE_DOWN.value, Item.FLOOR.value,
                    Item.FLOOR.value, Item.KEY_DOOR_CLOSED.value, Item.KEY.value, Item.DIAMOND.value, Item.WALL.value],
                # row 11
                [Item.WALL.value, Item.FLOOR.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.KEY.value, Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value],
                # row 12
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value]
            ]
        elif level == "4":
            matrix = [
                # row 0
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value],
                # row 1
                [Item.WALL.value, Item.FLOOR.value, Item.INDIANA.value, Item.FLOOR.value, Item.FLOOR.value,
                    Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value],
                # row 2
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.ROCK.value, Item.WALL.value, Item.WALL.value, Item.WALL.value],
                # row 3
                [Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value, Item.DIAMOND.value, Item.DIAMOND.value,
                    Item.FLOOR.value, Item.HOLE.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value],
                # row 4
                [Item.WALL.value, Item.ROCK.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value],
                # row 5
                [Item.WALL.value, Item.HOLE.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value,
                    Item.ROCK.value, Item.FLOOR.value, Item.DIAMOND.value, Item.FLOOR.value, Item.WALL.value],
                # row 6
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.DIAMOND.value, Item.WALL.value, Item.WALL.value, Item.WALL.value],
                # row 7
                [Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value,
                    Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value],
                # row 8
                [Item.WALL.value, Item.FLOOR.value, Item.ROCK.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value,
                    Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value],
                # row 9
                [Item.WALL.value, Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value, Item.ROCK.value,
                    Item.WALL.value, Item.HOLE.value, Item.WALL.value, Item.FLOOR.value, Item.WALL.value],
                # row 10
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.HOLE.value, Item.DIAMOND.value,
                    Item.WALL.value, Item.EXIT.value, Item.WALL.value, Item.FLOOR.value, Item.WALL.value],
                # row 11
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.DIAMOND.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.FLOOR.value, Item.WALL.value],
                # row 12
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value]
            ]
        elif level == "5":
            matrix = [
                # row 0
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value],
                # row 1
                [Item.WALL.value, Item.EXIT.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.DIAMOND.value, Item.DIAMOND.value, Item.WALL.value],
                # row 2
                [Item.WALL.value, Item.INDIANA.value, Item.PYKE_DOWN.value, Item.FLOOR.value, Item.FLOOR.value, Item.KEY.value,
                    Item.WALL.value, Item.DIAMOND.value, Item.DIAMOND.value, Item.WALL.value],
                # row 3
                [Item.WALL.value, Item.PYKE_DOWN.value, Item.WALL.value, Item.WALL.value, Item.ROCK.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.KEY_DOOR_CLOSED.value, Item.WALL.value],
                # row 4
                [Item.WALL.value, Item.DIAMOND.value, Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value,
                    Item.FLOOR.value, Item.WALL.value, Item.WALL.value, Item.HOLE.value, Item.WALL.value],
                # row 5
                [Item.WALL.value, Item.DIAMOND.value, Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value,
                    Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value],
                # row 6
                [Item.WALL.value, Item.HOLE.value, Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value,
                    Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value],
                # row 7
                [Item.WALL.value, Item.FLOOR.value, Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value,
                    Item.FLOOR.value, Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value],
                # row 8
                [Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.FLOOR.value, Item.WALL.value],
                # row 9
                [Item.WALL.value, Item.LAVA.value, Item.LAVA.value, Item.LAVA.value, Item.FLOOR.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.ROCK.value, Item.WALL.value],
                # row 10
                [Item.WALL.value, Item.LAVA.value, Item.LAVA.value, Item.LAVA.value, Item.FLOOR.value,
                    Item.PYKE_DOWN.value, Item.PYKE_DOWN.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value],
                # row 11
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.DIAMOND.value, Item.DIAMOND.value, Item.WALL.value, Item.WALL.value, Item.WALL.value],
                # row 12
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value]
            ]

        elif level == "6":
            matrix = [
                # row 0
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value],
                # row 1
                [Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value,
                    Item.INDIANA.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value],
                # row 2
                [Item.WALL.value, Item.FLOOR.value, Item.ROCK.value, Item.FLOOR.value, Item.DIAMOND.value, Item.DIAMOND.value,
                    Item.FLOOR.value, Item.ROCK.value, Item.KEY.value, Item.WALL.value],
                # row 3
                [Item.WALL.value, Item.HOLE.value, Item.WALL.value, Item.FLOOR.value, Item.WALL.value,
                    Item.WALL.value, Item.FLOOR.value, Item.WALL.value, Item.HOLE.value, Item.WALL.value],
                # row 4
                [Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value,
                    Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value],
                # row 5
                [Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value,
                    Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value],
                # row 6
                [Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value, Item.WALL.value,
                    Item.KEY_DOOR_CLOSED.value, Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value],
                # row 7
                [Item.WALL.value, Item.FLOOR.value, Item.DIAMOND.value, Item.WALL.value, Item.EXIT.value,
                    Item.DIAMOND.value, Item.WALL.value, Item.FLOOR.value, Item.DIAMOND.value, Item.WALL.value],
                # row 8
                [Item.WALL.value, Item.WALL.value, Item.KEY_DOOR_CLOSED.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.PYKE_DOWN.value, Item.WALL.value, Item.WALL.value],
                # row 9
                [Item.WALL.value, Item.HOLE.value, Item.FLOOR.value, Item.DIAMOND.value, Item.DIAMOND.value,
                    Item.DIAMOND.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value],
                # row 10
                [Item.WALL.value, Item.FLOOR.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.PYKE_DOWN.value, Item.WALL.value],
                # row 11
                [Item.WALL.value, Item.PYKE_DOWN.value, Item.FLOOR.value, Item.DIAMOND.value, Item.KEY.value,
                    Item.DIAMOND.value, Item.FLOOR.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value],
                # row 12
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value]
            ]

        elif level == "7":
            matrix = [
                # row 0
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value],
                # row 1
                [Item.WALL.value, Item.WALL.value, Item.ROCK.value, Item.FLOOR.value, Item.ROCK.value,
                    Item.FLOOR.value, Item.WALL.value, Item.WALL.value, Item.FLOOR.value, Item.WALL.value],
                # row 2
                [Item.WALL.value, Item.ROCK.value, Item.INDIANA.value, Item.ROCK.value, Item.FLOOR.value, Item.ROCK.value,
                    Item.FLOOR.value, Item.WALL.value, Item.FLOOR.value, Item.WALL.value],
                # row 3
                [Item.WALL.value, Item.FLOOR.value, Item.ROCK.value, Item.WALL.value, Item.DIAMOND.value,
                    Item.WALL.value, Item.ROCK.value, Item.WALL.value, Item.DIAMOND.value, Item.WALL.value],
                # row 4
                [Item.WALL.value, Item.ROCK.value, Item.FLOOR.value, Item.ROCK.value, Item.FLOOR.value,
                    Item.ROCK.value, Item.WALL.value, Item.WALL.value, Item.ROCK.value, Item.WALL.value],
                # row 5
                [Item.WALL.value, Item.WALL.value, Item.ROCK.value, Item.FLOOR.value, Item.HOLE.value,
                    Item.FLOOR.value, Item.WALL.value, Item.KEY.value, Item.DIAMOND.value, Item.WALL.value],
                # row 6
                [Item.WALL.value, Item.FLOOR.value, Item.DIAMOND.value, Item.FLOOR.value, Item.WALL.value,
                    Item.ROCK.value, Item.WALL.value, Item.FLOOR.value, Item.ROCK.value, Item.WALL.value],
                # row 7
                [Item.WALL.value, Item.ROCK.value, Item.WALL.value, Item.WALL.value, Item.ROCK.value,
                    Item.FLOOR.value, Item.WALL.value, Item.FLOOR.value, Item.DIAMOND.value, Item.WALL.value],
                # row 8
                [Item.WALL.value, Item.HOLE.value, Item.ROCK.value, Item.FLOOR.value, Item.FLOOR.value,
                    Item.DIAMOND.value, Item.FLOOR.value, Item.FLOOR.value, Item.HOLE.value, Item.WALL.value],
                # row 9
                [Item.WALL.value, Item.FLOOR.value, Item.FLOOR.value, Item.WALL.value, Item.WALL.value,
                    Item.KEY_DOOR_CLOSED.value, Item.WALL.value, Item.WALL.value, Item.ROCK.value, Item.WALL.value],
                # row 10
                [Item.WALL.value, Item.DIAMOND.value, Item.FLOOR.value, Item.WALL.value, Item.FLOOR.value,
                    Item.DIAMOND.value, Item.FLOOR.value, Item.WALL.value, Item.FLOOR.value, Item.WALL.value],
                # row 11
                [Item.WALL.value, Item.FLOOR.value, Item.WALL.value, Item.WALL.value, Item.FLOOR.value,
                    Item.EXIT.value, Item.FLOOR.value, Item.WALL.value, Item.ROCK.value, Item.WALL.value],
                # row 12
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value]
            ]

        elif level == "8":
            matrix = [
                # row 0
                [Item.WALL.value, Item.WALL.value, Item.DIAMOND.value, Item.FLOOR.value, Item.DIAMOND.value,
                    Item.FLOOR.value, Item.DIAMOND.value, Item.FLOOR.value, Item.WALL.value, Item.WALL.value],
                # row 1
                [Item.WALL.value, Item.WALL.value, Item.FLOOR.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.DIAMOND.value, Item.WALL.value, Item.WALL.value],
                # row 2
                [Item.WALL.value, Item.WALL.value, Item.DIAMOND.value, Item.WALL.value, Item.FLOOR.value, Item.EXIT.value,
                    Item.WALL.value, Item.FLOOR.value, Item.WALL.value, Item.WALL.value],
                # row 3
                [Item.WALL.value, Item.WALL.value, Item.FLOOR.value, Item.DIAMOND.value, Item.FLOOR.value,
                    Item.DIAMOND.value, Item.WALL.value, Item.FLOOR.value, Item.WALL.value, Item.WALL.value],
                # row 4
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.KEY_DOOR_CLOSED.value, Item.WALL.value, Item.WALL.value],
                # row 5
                [Item.WALL.value, Item.WALL.value, Item.BUTTOM.value, Item.FLOOR.value, Item.ROCK.value,
                    Item.INDIANA.value, Item.FLOOR.value, Item.DIAMOND.value, Item.WALL.value, Item.WALL.value],
                # row 6
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.BUTTOM_DOOR_CLOSED.value, Item.WALL.value, Item.WALL.value],
                # row 7
                [Item.WALL.value, Item.WALL.value, Item.HOLE.value, Item.ROCK.value, Item.DIAMOND.value,
                    Item.PYKE_DOWN.value, Item.BUTTOM_DOOR_CLOSED.value, Item.FLOOR.value, Item.WALL.value, Item.WALL.value],
                # row 8
                [Item.WALL.value, Item.WALL.value, Item.KEY.value, Item.WALL.value, Item.PYKE_DOWN.value,
                    Item.PYKE_DOWN.value, Item.WALL.value, Item.FLOOR.value, Item.WALL.value, Item.WALL.value],
                # row 9
                [Item.WALL.value, Item.WALL.value, Item.ROCK.value, Item.WALL.value, Item.PYKE_DOWN.value,
                    Item.PYKE_DOWN.value, Item.WALL.value, Item.PYKE_DOWN.value, Item.WALL.value, Item.WALL.value],
                # row 10
                [Item.WALL.value, Item.WALL.value, Item.HOLE.value, Item.ROCK.value, Item.FLOOR.value,
                    Item.DIAMOND.value, Item.BUTTOM.value, Item.DIAMOND.value, Item.WALL.value, Item.WALL.value],
                # row 11
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value],
                # row 12
                [Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value,
                    Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value, Item.WALL.value]
            ]

        return np.array(matrix)

    def save_matrix(self, matrix, path):
        np.savetxt(path, matrix, fmt='%d')

    def load_matrix(self, path):
        return np.loadtxt(path, dtype=int)


if __name__ == "__main__":
    classifier_utility = ClassifierUtility()
    # save a level
    level = input("Enter the level number: ")
    matrix = classifier_utility.get_matrix(level)
    path_to_matrix = "./resources/levels/matrices/l" + level + ".txt"
    classifier_utility.save_matrix(matrix, path_to_matrix)

    # read a level
    level_matrix = classifier_utility.load_matrix(path_to_matrix)
    print(level_matrix)
