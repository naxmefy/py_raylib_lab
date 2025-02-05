from pyray import *
from raylib import *

init_window(850, 400, "000 First")

while not window_should_close():
    begin_drawing()
    clear_background(RAYWHITE)
    draw_text("Congrats! You created your first window!", 190, 200, 20, LIGHTGRAY)
    end_drawing()

close_window()
