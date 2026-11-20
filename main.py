import pygame
import sys
from constants import *
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


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
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable) # type: ignore[attr-defined]
    Asteroid.containers = (asteroids, updatable, drawable) # type: ignore[attr-defined]
    AsteroidField.containers = (updatable) # type: ignore[attr-defined]
    Shot.containers = (updatable,drawable,shots) # type: ignore[attr-defined]

    dt = 0
    score = 0
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
                print("Game over!Respawning..")
                player.kill()
                player = Player(SCREEN_WIDTH/2 , SCREEN_HEIGHT/2 )
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    score += 1
                    print("Current-score",score)

        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)

        #print(dt)
        pygame.display.flip()

if __name__ == "__main__":
    main()
