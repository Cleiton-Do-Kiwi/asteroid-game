import pygame
import sys
from constants import *
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}!")
    print(f"""
        Screen width: {SCREEN_WIDTH}
        Screen height: {SCREEN_HEIGHT}
        """)
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable) # type: ignore[attr-defined]
    Asteroid.containers = (asteroids, updatable, drawable) # type: ignore[attr-defined]
    AsteroidField.containers = (updatable)

    dt = 0
    player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2 )
    asteroid_field = AsteroidField()

    while True:
        dt = clock.tick(60) / 1000
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()


        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)

        #print(dt)
        pygame.display.flip()

if __name__ == "__main__":
    main()
