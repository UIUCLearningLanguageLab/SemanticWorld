class World:
    dimensions = (500, 500)
    num_entities = 10
    time_steps = 1000

class Entity:
    color_options = ["red", "green", "blue", "yellow", "magenta", "cyan", "white", "black"]
    dimensions = (20, 30)
    speed = 10

class Display:
    dimensions = (640, 480)
    bg_color = (128, 128, 128)