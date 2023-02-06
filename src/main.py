import pygame

# Initialize pygame, otherwise the functions won't work
pygame.init()

screen = pygame.display.set_mode((800,600))

# Game loop
# Variable needed for while true loop
continue_running = True
while continue_running:
  # For loop to go through all events in pygame
  for event in pygame.event.get():
    # Event to quit found, then quit
    if event.type == pygame.QUIT:
      continue_running = False