import pygame
import random

# Player object
class Player:
  def __init__(self, player_number, image_name):
    self.player_number = player_number
    # Set the desired x and y coordinates
    self.x = 100
    self.y = 225
    if player_number == 1:
      self.x = 1000
    # Load image
    self.image = pygame.image.load(image_name)
    # Used to control speed
    self.speed_rate = 0.0

  def blit_image(self, screen):
    screen.blit(self.image, (self.x, self.y))

  def change_speed_rate(self, direction):
    # Assume down
    self.speed_rate = 0.2
    # Change to up if needed
    if (direction == 'up'):
      self.speed_rate = -0.2

  def stop_speed_rate(self):
    self.speed_rate = 0.0

  def move(self):
    self.y += self.speed_rate
    # Border collission
    # 600px - 128px = 472
    if self.y > 472:
      self.y = 472
    if self.y < 0:
      self.y = 0

# Ball object
class Ball:
  def __init__(self):
    # 475 and 625 for each player's x values
    self.x = 475
    self.y = 300
    # Load image
    self.image = pygame.image.load('img/ball.png')
    # Used to control speed
    self.x_speed_rate = 0.0
    self.y_speed_rate = 0.0

  def blit_image(self, screen):
    screen.blit(self.image, (self.x, self.y))

  def reset(self, winner):
    # Random y value
    self.y = random.randint(100, 500)
    # Static x value for each player
    self.x = 475
    if winner == "second player":
      self.x = 625

  # TODO(Luis): Figure out ball movement
  def change_speed_rate(self):
    pass

  def move(self):
    self.x += self.x_speed_rate
    self.y += self.y_speed_rate

  def check_border_collision(self):
    pass

  def check_player_collision(self, player):
    return True