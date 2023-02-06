import pygame

# Player object
class Player:
  def __init__(self, player_number, image_name):
    self.player_number = player_number
    # Set the desired x and y coordinates
    if player_number == 0:
      self.x = 100
      self.y = 100
    else:
      self.x = 1000
      self.y = 100
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
