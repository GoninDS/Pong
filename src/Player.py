# Player object

class Player:
  def __init__(self, player_number):
    self.player_number = player_number
    if player_number == 0:
      self.x = 0
      self.y = 0
    else:
      self.x = 10
      self.y = 10

  def blit_image():
    pass

  def move_upwards(self):
    pass

  def move_downwards(self):
    pass

player0 = Player(0)
player1 = Player(1)