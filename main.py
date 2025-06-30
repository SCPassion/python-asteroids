import pygame
from constants import *
from player import Player

def main():

  # Initialize the game window
  pygame.init()

  # Set up the display
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  
  #Initialize a player object
  player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

  # Set delta time for the game loop
  clock = pygame.time.Clock()
  dt = 0

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      
    screen.fill((0, 0, 0))  # Fill the screen with black
    player.draw(screen)  # Draw the player

    pygame.display.flip()  # Update the display
    waited = clock.tick(60)  # Limit the frame rate to 60 FPS
    dt = waited / 1000.0  # Convert milliseconds to seconds

if __name__ == "__main__":
  main()