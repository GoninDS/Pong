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
      self.x = 100
      self.y = 100
    # Load image
    self.image = pygame.image.load(image_name)

  def blit_image(self, screen):
    screen.blit(self.image, (self.x, self.y))

  def move_upwards(self):
    pass

  def move_downwards(self):
    pass