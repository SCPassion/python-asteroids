import pygame
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot
import sys
def main():
  # Initialize the game window
  pygame.init()

  # Set up the display
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  
  # Set delta time for the game loop
  clock = pygame.time.Clock()

  # Groups for managing sprites
  updateable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Asteroid.containers = (asteroids, updateable, drawable)
  AsteroidField.containers = updateable
  Shot.containers = (shots, updateable, drawable)
  
  # Initialize the asteroid field
  asteroid_field = AsteroidField()

  Player.containers = (updateable, drawable)  # Set the containers for the Player class

  #Initialize a player object
  player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

  dt = 0

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      
    updateable.update(dt)  # Update all sprites in the updateable group
    screen.fill((0, 0, 0))  # Fill the screen with black

    for obj in drawable:
      obj.draw(screen)

    for shot in shots:
      shot.draw(screen)

    pygame.display.flip()  # Update the display
    waited = clock.tick(60)  # Limit the frame rate to 60 FPS
    dt = waited / 1000.0  # Convert milliseconds to seconds

    for asteroid in asteroids:
      if player.collide(asteroid):
        print("Game Over!")
        pygame.quit()
        sys.exit()

      for shot in shots:
        if shot.collide(asteroid):
          asteroid.split()
          shot.kill()

if __name__ == "__main__":
  main()