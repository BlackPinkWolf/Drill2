from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while(1):    
    x = 0
    while(x < 800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x = x + 2
        delay(0.01)

    y = 0
    while(y < 600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(800,y)
        y = y + 2
        delay(0.01)

    x = 800
    while(x > 0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,600)
        x = x - 2
        delay(0.01)

    y = 600
    while(y > 0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(0,y)
        y = y - 2
        delay(0.01)

    x = 0
    while(x < 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x = x + 2
        delay(0.01)

    x = 0
    y = 1
    while(x < 360):
        angle_in_degrees = x
        angle_in_radians = math.radians(angle_in_degrees)
        sin_value = math.sin(angle_in_radians) * 200 + 400
        angle_in_degrees1 = y
        angle_in_radians1 = math.radians(angle_in_degrees1)
        sin_value1 = math.cos(angle_in_radians1) * 200 + 300
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(sin_value, sin_value1)
        x = x + 2
        y = y + 2
        delay(0.01)

close_canvas()
