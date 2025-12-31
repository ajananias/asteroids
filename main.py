import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys
def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    Player.containers = (updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    while True:
        for event in pygame.event.get(): # this makes the close button work
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)

        for sprite in asteroids:
            if sprite.check_collision(player):
                print("Game over!")
                sys.exit()
            
        for sprite in shots:
            for asteroid in asteroids:
                if sprite.check_collision(asteroid):
                    sprite.kill()
                    asteroid.split()
            
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()