import numpy as np

from indiana.classifiers.classifier import ItemCategory


class ClassifierUtility():

    def __init__(self):
        pass

    def get_matrix(self, level):
        if level == "1":
            matrix = [
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.PLAYER.value, ItemCategory.DIAMOND.value, ItemCategory.DIAMOND.value,
                    ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value,
                    ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value,
                    ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value,
                    ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.EXIT.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value,
                    ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value]
            ]

        elif level == "2":
            matrix = [
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value,
                    ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.PYKE.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.PYKE.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value,
                    ItemCategory.PYKE.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.EXIT.value, ItemCategory.BARRIER.value,
                    ItemCategory.PYKE.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.DIAMOND.value, ItemCategory.DIAMOND.value, ItemCategory.PYKE.value, ItemCategory.PYKE.value,
                    ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.PLAYER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.DIAMOND.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value]
            ]

        elif level == "3":
            matrix = [
                # row 0
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 1
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value,
                    ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value],
                # row 2
                [ItemCategory.BARRIER.value, ItemCategory.PLAYER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value,
                    ItemCategory.KEY_DOOR.value, ItemCategory.FLOOR.value, ItemCategory.EXIT.value, ItemCategory.BARRIER.value],
                # row 3
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.PYKE.value, ItemCategory.FLOOR.value,
                    ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value],
                # row 4
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.PYKE.value, ItemCategory.BARRIER.value, ItemCategory.KEY_DOOR.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 5
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value,
                    ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.DIAMOND.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value],
                # row 6
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value,
                    ItemCategory.FLOOR.value, ItemCategory.KEY_DOOR.value, ItemCategory.KEY.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value],
                # row 7
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value,
                    ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.DIAMOND.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value],
                # row 8
                [ItemCategory.BARRIER.value, ItemCategory.KEY.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.DIAMOND.value,
                    ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 9
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value,
                    ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 10
                [ItemCategory.BARRIER.value, ItemCategory.DIAMOND.value, ItemCategory.PYKE.value, ItemCategory.PYKE.value, ItemCategory.FLOOR.value,
                    ItemCategory.FLOOR.value, ItemCategory.KEY_DOOR.value, ItemCategory.KEY.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value],
                # row 11
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.KEY.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 12
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value]
            ]
        elif level == "4":
            matrix = [
                # row 0
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 1
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.PLAYER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value,
                    ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 2
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.ROCK.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 3
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.DIAMOND.value,
                    ItemCategory.FLOOR.value, ItemCategory.HOLE.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 4
                [ItemCategory.BARRIER.value, ItemCategory.ROCK.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 5
                [ItemCategory.BARRIER.value, ItemCategory.HOLE.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value,
                    ItemCategory.ROCK.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 6
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 7
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value,
                    ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 8
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.ROCK.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value,
                    ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 9
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.ROCK.value,
                    ItemCategory.BARRIER.value, ItemCategory.HOLE.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 10
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.HOLE.value, ItemCategory.DIAMOND.value,
                    ItemCategory.BARRIER.value, ItemCategory.EXIT.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 11
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.DIAMOND.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 12
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value]
            ]
        elif level == "5":
            matrix = [
                # row 0
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 1
                [ItemCategory.BARRIER.value, ItemCategory.EXIT.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.DIAMOND.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value],
                # row 2
                [ItemCategory.BARRIER.value, ItemCategory.PLAYER.value, ItemCategory.PYKE.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.KEY.value,
                    ItemCategory.BARRIER.value, ItemCategory.DIAMOND.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value],
                # row 3
                [ItemCategory.BARRIER.value, ItemCategory.PYKE.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.ROCK.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.KEY_DOOR.value, ItemCategory.BARRIER.value],
                # row 4
                [ItemCategory.BARRIER.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value,
                    ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.HOLE.value, ItemCategory.BARRIER.value],
                # row 5
                [ItemCategory.BARRIER.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value,
                    ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 6
                [ItemCategory.BARRIER.value, ItemCategory.HOLE.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value,
                    ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 7
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value,
                    ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 8
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 9
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.ROCK.value, ItemCategory.BARRIER.value],
                # row 10
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value,
                    ItemCategory.PYKE.value, ItemCategory.PYKE.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 11
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.DIAMOND.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 12
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value]
            ]

        elif level == "6":
            matrix = [
                # row 0
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 1
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value,
                    ItemCategory.PLAYER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 2
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.ROCK.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.DIAMOND.value,
                    ItemCategory.FLOOR.value, ItemCategory.ROCK.value, ItemCategory.KEY.value, ItemCategory.BARRIER.value],
                # row 3
                [ItemCategory.BARRIER.value, ItemCategory.HOLE.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.HOLE.value, ItemCategory.BARRIER.value],
                # row 4
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value,
                    ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 5
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value,
                    ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 6
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.KEY_DOOR.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 7
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value, ItemCategory.EXIT.value,
                    ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value],
                # row 8
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.KEY_DOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.PYKE.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 9
                [ItemCategory.BARRIER.value, ItemCategory.HOLE.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.DIAMOND.value,
                    ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 10
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.PYKE.value, ItemCategory.BARRIER.value],
                # row 11
                [ItemCategory.BARRIER.value, ItemCategory.PYKE.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.KEY.value,
                    ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 12
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value]
            ]

        elif level == "7":
            matrix = [
                # row 0
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 1
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.ROCK.value, ItemCategory.FLOOR.value, ItemCategory.ROCK.value,
                    ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 2
                [ItemCategory.BARRIER.value, ItemCategory.ROCK.value, ItemCategory.PLAYER.value, ItemCategory.ROCK.value, ItemCategory.FLOOR.value, ItemCategory.ROCK.value,
                    ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 3
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.ROCK.value, ItemCategory.BARRIER.value, ItemCategory.DIAMOND.value,
                    ItemCategory.BARRIER.value, ItemCategory.ROCK.value, ItemCategory.BARRIER.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value],
                # row 4
                [ItemCategory.BARRIER.value, ItemCategory.ROCK.value, ItemCategory.FLOOR.value, ItemCategory.ROCK.value, ItemCategory.FLOOR.value,
                    ItemCategory.ROCK.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.ROCK.value, ItemCategory.BARRIER.value],
                # row 5
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.ROCK.value, ItemCategory.FLOOR.value, ItemCategory.HOLE.value,
                    ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.KEY.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value],
                # row 6
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value,
                    ItemCategory.ROCK.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.ROCK.value, ItemCategory.BARRIER.value],
                # row 7
                [ItemCategory.BARRIER.value, ItemCategory.ROCK.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.ROCK.value,
                    ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value],
                # row 8
                [ItemCategory.BARRIER.value, ItemCategory.HOLE.value, ItemCategory.ROCK.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value,
                    ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.HOLE.value, ItemCategory.BARRIER.value],
                # row 9
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.KEY_DOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.ROCK.value, ItemCategory.BARRIER.value],
                # row 10
                [ItemCategory.BARRIER.value, ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value,
                    ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value],
                # row 11
                [ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value,
                    ItemCategory.EXIT.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.ROCK.value, ItemCategory.BARRIER.value],
                # row 12
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value]
            ]

        elif level == "8":
            matrix = [
                # row 0
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value,
                    ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 1
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 2
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.EXIT.value,
                    ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 3
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.FLOOR.value,
                    ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 4
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.KEY_DOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 5
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BUTTOM.value, ItemCategory.FLOOR.value, ItemCategory.ROCK.value,
                    ItemCategory.PLAYER.value, ItemCategory.FLOOR.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 6
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BUTTOM_DOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 7
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.HOLE.value, ItemCategory.ROCK.value, ItemCategory.DIAMOND.value,
                    ItemCategory.PYKE.value, ItemCategory.BUTTOM_DOOR.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 8
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.KEY.value, ItemCategory.BARRIER.value, ItemCategory.PYKE.value,
                    ItemCategory.PYKE.value, ItemCategory.BARRIER.value, ItemCategory.FLOOR.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 9
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.ROCK.value, ItemCategory.BARRIER.value, ItemCategory.PYKE.value,
                    ItemCategory.PYKE.value, ItemCategory.BARRIER.value, ItemCategory.PYKE.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 10
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.HOLE.value, ItemCategory.ROCK.value, ItemCategory.FLOOR.value,
                    ItemCategory.DIAMOND.value, ItemCategory.BUTTOM.value, ItemCategory.DIAMOND.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 11
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value],
                # row 12
                [ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value,
                    ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value, ItemCategory.BARRIER.value]
            ]

        return np.array(matrix)

    def save_matrix(self, matrix, path):
        np.savetxt(path, matrix, fmt='%d')

    def load_matrix(self, path):
        return np.loadtxt(path, dtype=int)


if __name__ == "__main__":
    classifier_utility = ClassifierUtility()
    # save a level
    max_level = 8
    for i in range(1, max_level+1):
        level = str(i)
        matrix = classifier_utility.get_matrix(level)
        path_to_matrix = "./resources/levels/matrices/l" + level + ".txt"
        classifier_utility.save_matrix(matrix, path_to_matrix)
        # read a level
        level_matrix = classifier_utility.load_matrix(path_to_matrix)
        print(level_matrix)
