import pygame
import sys
import pygame

class Display:

    def __init__(self, screen_params, the_world):

        self.the_world = the_world

        self.screen = None
        self.running = None
        self.dimensions = screen_params.dimensions

        self.create_screen()
        self.draw_entities()
        self.run_world()

    def run_world(self):
        # Main loop
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # Fill the screen with a color (optional)

            # Update the display
            pygame.display.flip()
        # Quit pygame
        pygame.quit()

    def create_screen(self):
    # Initialize pygame
        pygame.init()
        # Create the window
        self.screen = pygame.display.set_mode((self.dimensions[0], self.dimensions[1]))
        # Set window title
        pygame.display.set_caption("Semantic World")
        self.screen.fill((128, 128, 128))  # Grey background

    def draw_entities(self):
        for entity in self.the_world.entity_list:
            pygame.draw.rect(self.screen,
                             entity.color,
                             (entity.position[0],
                              entity.position[1],
                              entity.dimensions[0],
                              entity.dimensions[1]))
#
# import pygame
# import sys
# # Initialize pygame
# pygame.init()
# # Set up window dimensions
# window_width = 640
# window_height = 480
# # Set the rectangle dimensions and position
# rect_x = 100  # x position of the rectangle
# rect_y = 100  # y position of the rectangle
# rect_width = 200  # width of the rectangle
# rect_height = 150  # height of the rectangle
# # Create the window
# screen = pygame.display.set_mode((window_width, window_height))
# # Set window title
# pygame.display.set_caption("Pygame Window with Rectangle")
# # Main loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     # Fill the screen with a grey color
#     screen.fill((128, 128, 128))  # Grey background
#     # Draw a red rectangle
#     pygame.draw.rect(screen, (255, 0, 0), (rect_x, rect_y, rect_width, rect_height))
#     # Update the display
#     pygame.display.flip()
# # Quit pygame
# pygame.quit()
# sys.exit()