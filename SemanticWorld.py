from src.display import display
from src import world

if __name__ == "__main__" :

    the_world = world.World()

    for i in range(30):
        the_world.next()