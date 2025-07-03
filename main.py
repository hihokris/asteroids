import pygame
from player import Player
from constants import *
from asteroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots,updateable,drawable)
    Player.containers = (updateable,drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    player_obj = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    field_obj = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")

        #player_obj.draw(screen)
        #player_obj.update(dt)
        for item in updateable:
            item.update(dt)
        for asteriter in asteroids:
            for shotiter in shots:
                if asteriter.collision_detect(shotiter):
                    shotiter.kill()
                    asteriter.split()
            if player_obj.collision_detect(asteriter):
                print("Game over!")
                return

        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000 #tick the clock
        #print(dt)

if __name__ == "__main__":
    main()
