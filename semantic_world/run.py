from src import world
from config import config

def main():
    the_world = world.World(config.World)
    print(the_world)

if __name__ == "__main__" :
    main()