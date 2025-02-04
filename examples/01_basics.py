from pyray import *
from raylib import *
from os.path import join

init_window(850, 400, "Basics")

while not window_should_close():
    begin_drawing()
    clear_background(RAYWHITE)
    end_drawing()

close_window()
