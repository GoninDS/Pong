# Import pygame
import pygame
# Import the player object
from classes import Player
from classes import Ball

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

# Create ball
ball = Ball()
# ball2 = Ball(0)

# Loop to go through pygame events
def loop_events():
  # For loop to go through all events in pygame
  for event in pygame.event.get():
    # Event to quit
    if event.type == pygame.QUIT:
      return False
    # Check for a keypress
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN:
        second_player.change_speed_rate('down')
      if event.key == pygame.K_UP:
        second_player.change_speed_rate('up')
      if event.key == pygame.K_s:
        first_player.change_speed_rate('down')
      if event.key == pygame.K_w:
        first_player.change_speed_rate('up')
    # Key release
    if event.type == pygame.KEYUP:
      # Either arrow
      if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
        second_player.stop_speed_rate()
      # S or W
      if event.key == pygame.K_s or event.key == pygame.K_w:
        first_player.stop_speed_rate()
  # Event to quit not found
  return True

# Checks collission between players, border and the ball
def check_collision():
  ball.check_border_collision()
  ball.check_player_collision(first_player)
  ball.check_player_collision(second_player)

# Update game image
def update_game_image():
  first_player.blit_image(screen)
  second_player.blit_image(screen)
  ball.blit_image(screen)
  # ball2.blit_image(screen)
  pygame.display.update()

# Game loop
continue_running = True

while continue_running:
  # Add background
  screen.blit(background, (0,0))
  # Loop through pygame events
  continue_running = loop_events()
  # Move the players
  first_player.move()
  second_player.move()
  # Move the ball
  ball.move()
  # Check collision between players, border and the ball
  check_collision()
  # Window must be updated
  update_game_image()
  