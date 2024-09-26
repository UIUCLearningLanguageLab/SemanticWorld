from src import world
from config import config
from src.display import display

def main():
    the_world = world.World(config.World, config.Entity)
    the_display = display.Display(config.Display, the_world)
    the_world.run()

if __name__ == "__main__" :
    main()