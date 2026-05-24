import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from logger import log_state, log_event

def main():
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	updatable, drawable, asteroids, shots = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = ( asteroids, updatable, drawable )
	AsteroidField.containers = ( updatable )
	Shot.containers = ( updatable, drawable, shots )

	clock = pygame.time.Clock()
	dt = 0.0

	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	asteroidfield = AsteroidField()

	running: bool = True

	while running:
		log_state()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return 

		screen.fill("Black")
		for member in updatable:
			member.update(dt)
		for member in drawable:
			member.draw(screen)

		for index, asteroid in enumerate(asteroids):
			if asteroid.collides_with(player):
				log_event("player_hit")
				print("Game over!")
				sys.exit(1)

			for shot in shots:
				if asteroid.collides_with(shot):
					log_event("asteroid_shot")
					asteroid.split()


		pygame.display.flip()
		dt = clock.tick(60) / 1000
		
	
	


if __name__ == "__main__":
    main()
