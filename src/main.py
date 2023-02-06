# Import pygame
import pygame
# Import the player object
from Player import Player

# Initialize pygame
pygame.init()

# Setup the screen
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Pong")

first_player = Player(1, 'alien.png')

# Game loop
continue_running = True
while continue_running:
  # For loop to go through all events in pygame
  for event in pygame.event.get():
    # Event to quit
    if event.type == pygame.QUIT:
      continue_running = False

    # Window must be updated
    first_player.blit_image(screen)
    pygame.display.update()