from PyQt5.QtCore import Qt

#window

window_width = 1200
window_height = 800

window_x_margin = 100
window_y_margin = 100

window_title = 'Random strike'

#paint timer

paint_timer_delay = 40 #ms

#player

player_hp = 3
player_speed = 500 #px per second

first_player_up = Qt.Key_W
first_player_down = Qt.Key_S
first_player_left = Qt.Key_A
first_player_right = Qt.Key_D

second_player_up = Qt.Key_Up
second_player_down = Qt.Key_Down
second_player_left = Qt.Key_Left
second_player_right = Qt.Key_Right


#action timer

action_timer_delay = 15

#maps
sample_map = 'maps/sample.map'

#camera

camera_divider_width = 50
