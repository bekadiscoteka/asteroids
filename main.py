import pygame
from constants import *
from logger import log_state
from player import *

def main():
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	updatable, drawable  = pygame.sprite.Group(), pygame.sprite.Group()
	Player.containers = (updatable, drawable)

	clock = pygame.time.Clock()
	dt = 0.0

	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

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
		pygame.display.flip()
		dt = clock.tick(60) / 1000
		
	
	


if __name__ == "__main__":
    main()
