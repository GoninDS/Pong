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
    # Create a rect for collission
    self.player_rect = pygame.Surface.get_rect(self.image)
    # Used to control speed
    self.speed_rate = 0.0
    # Points scored
    self.points_scored = 0

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
    # Create a rect for collission
    self.ball_rect = pygame.Surface.get_rect(self.image)
    # Used to control speed
    self.x_speed_rate = -0.1
    self.y_speed_rate = -0.2
    # Controls which side the ball last was
    self.side = "right"

  def blit_image(self, screen):
    screen.blit(self.image, (self.x, self.y))

  def reset(self):
    # Random y value
    self.y = random.randint(100, 500)
    if self.side == "right":
      # The ball is going to the left side
      self.side = "left"
      self.x = 625
      self.x_speed_rate = 0.1
    elif self.side == "left":
      self.side = "right"
      self.x = 475
      self.x_speed_rate = -0.1

  def move(self):
    self.x += self.x_speed_rate
    self.y += self.y_speed_rate

  def check_border_collision(self):
    if self.y <= 0:
      self.y_speed_rate = -1 * self.y_speed_rate
    elif self.y >= 600:
      self.y_speed_rate = -1 * self.y_speed_rate

  def check_point(self):
    if self.x <= 0:
      # Second player scored
      return "second"
    elif self.x >= 1100:
      # First player scored
      return "first"
    # None scored
    return "none"

  def check_player_collision(self, player):
    # Update x and y values for each rect
    self.ball_rect.x = self.x
    self.ball_rect.y = self.y
    player.player_rect.x = player.x
    player.player_rect.y = player.y
    if pygame.Rect.colliderect(self.ball_rect, player.player_rect):
      self.x_speed_rate = -1 * self.x_speed_rate