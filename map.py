from player import Player
from obstacle import Obstacle
from PyQt5.QtGui import QImage


def load_map(path):
    players = list()
    obstacles = list()
    bonuses = list()

    map = open(path)
    for line in map.readlines():
        if line.startswith('#'):
            continue

        line = line.replace('\n', '')
        tokens = line.split(' ')

        if len(tokens) == 0:
            continue

        if tokens[0] == 'map':
            for obstacle in _read_map(tokens):
                obstacles.append(obstacle)
        elif tokens[0] == 'player':
            players.append(_read_player(tokens))
        elif tokens[0] == 'obstacle':
            obstacles.append(_read_obstacle(tokens))
        elif tokens[0] == 'bonus':
            bonuses.append(_read_bonus(tokens))

    map.close()

    return players, obstacles, bonuses


def _read_map(tokens):
    borders = list()

    width = int(tokens[1])
    height = int(tokens[2])

    path = tokens[3]

    border_image = QImage(path)
    border_width = border_image.width()
    border_height = border_image.height()

    for x_num in range(width // border_width + 1):
        border = Obstacle(False, 0)
        border.x = x_num * border_width
        border.y = -border_height
        border.width = border_width
        border.height = border_height
        border.image = border_image

        borders.append(border)

    for x_num in range(width // border_width + 1):
        border = Obstacle(False, 0)
        border.x = x_num * border_width
        border.y = height
        border.width = border_width
        border.height = border_height
        border.image = border_image

        borders.append(border)

    for y_num in range(height // border_height + 1):
        border = Obstacle(False, 0)
        border.x = -border_width
        border.y = y_num * border_width
        border.width = border_width
        border.height = border_height
        border.image = border_image

        borders.append(border)

    for y_num in range(height // border_height + 1):
        border = Obstacle(False, 0)
        border.x = width
        border.y = y_num * border_width
        border.width = border_width
        border.height = border_height
        border.image = border_image

        borders.append(border)

    return borders


def _read_player(tokens):
    player = Player()
    player.x = int(tokens[1])
    player.y = int(tokens[2])
    player.set_image(tokens[3])

    return player


def _read_obstacle(tokens):
    is_destroyable = (tokens[3] == 'True')
    hit_count_to_destroy = int(tokens[4])

    obstacle = Obstacle(is_destroyable, hit_count_to_destroy)
    obstacle.x = int(tokens[1])
    obstacle.y = int(tokens[2])
    obstacle.set_image(tokens[5])

    return obstacle


def _read_bonus(tokens):
    pass
