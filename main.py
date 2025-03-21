# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    af = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                sys.exit("GAME OVER")
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()
                
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
