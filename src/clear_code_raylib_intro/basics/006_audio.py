from raylibpy import *
from os.path import join

init_window(1920, 1080, '006 Audio')
init_audio_device()
laser_sound = load_sound(join('assets', 'clear_code_raylib_intro', 'basics', 'laser.wav'))
play_sound(laser_sound)

music = load_music_stream(join('assets', 'clear_code_raylib_intro', 'basics', 'music.wav'))
play_music_stream(music)

while not window_should_close():
    update_music_stream(music)
    begin_drawing()
    clear_background(BLACK)
    end_drawing()

unload_music_stream(music)
close_audio_device()
close_window()
