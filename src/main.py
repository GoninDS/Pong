# Import pygame
import pygame
# Import the player object
from Player import Player

# Initialize pygame
pygame.init()

# Setup the screen
icon = pygame.image.load('img/icon.png')
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1100, 600))
pygame.display.set_caption("Pong")
background = pygame.image.load('img/background.png')

# Create players
first_player = Player(0, 'img/player_tile.png')
second_player = Player(1, 'img/player_tile.png')

# Game loop
continue_running = True
while continue_running:
  # Fill the screen with black
  screen.fill((0, 0, 0))
  screen.blit(background, (0,0))

  # For loop to go through all events in pygame
  for event in pygame.event.get():
    # Event to quit
    if event.type == pygame.QUIT:
      continue_running = False
    # Check for a keypress
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN:
        first_player.change_speed_rate('down')
      if event.key == pygame.K_UP:
        first_player.change_speed_rate('up')
    # Key release
    if event.type == pygame.KEYUP:
      # Either arrow
      if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
        first_player.stop_speed_rate()

  # Move the player
  first_player.move()
  # Window must be updated
  first_player.blit_image(screen)
  second_player.blit_image(screen)
  pygame.display.update()