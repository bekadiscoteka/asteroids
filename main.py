import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from logger import log_state, log_event

def draw_text(surface, text, font, color, x, y):
	text_surface = font.render(text, True, color)
	text_rect = text_surface.get_rect()
	text_rect.center = (x, y)
	surface.blit(text_surface, text_rect)


def main():
	print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
	print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	font = pygame.font.Font(None, 36)
# Purple placeholder

	updatable, drawable, asteroids, shots = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = ( asteroids, updatable, drawable )
	AsteroidField.containers = ( updatable )
	Shot.containers = ( updatable, drawable, shots )

	clock = pygame.time.Clock()
	dt = 0.0

	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	asteroidfield = AsteroidField()
	score: int = 0
	game_state: str = "MENU"

	running: bool = True

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_state = "GAME_OVER"

		if game_state == "PLAYING":
			log_state()
			screen.fill("Black")
			keys = pygame.key.get_pressed()
			if keys[pygame.K_ESCAPE]:
				return
			for member in updatable:
				member.update(dt)
			for member in drawable:
				member.draw(screen)

			for index, asteroid in enumerate(asteroids):
				if asteroid.collides_with(player):
					log_event("player_hit")
					print("Game over!")
					game_state = "GAME_OVER"

				for shot in shots:
					if asteroid.collides_with(shot):
						log_event("asteroid_shot")
						score += 1
						asteroid.split()
						shot.kill()

			score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
			screen.blit(score_surface, (20, 20))

		elif game_state == "GAME_OVER":
			log_state()
			screen.fill("Black")
			if score < 10:
				level = "GAY" 	
				color = (128, 0, 128) 
				prefix = "strongly recommended to"
			else: 
				prefix = ""
				level = "STRAIGHT"
				color = (0, 128, 255)
			draw_text(screen, "Game Over", font, (255, 0, 0), SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50)
			draw_text(screen, f"Final Score: {score}", font, (255, 255, 255), SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 10)
			draw_text(screen, "Press R to Restart", font, (255, 255, 255), SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 70)
			draw_text(screen, f"{prefix} Press ESC to Exit", font, (255, 255, 255), SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 130)
			draw_text(screen, f"your Level: {level}", font, color, SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 100)
			if score > 0:
				level

			keys = pygame.key.get_pressed()
			if keys[pygame.K_r]:
				score = 0
				main()
			elif keys[pygame.K_ESCAPE]:

				sys.exit()
		
		elif game_state == "MENU":
			log_state()
			screen.fill("Black")
			draw_text(screen, "Asteroids", font, (255, 255, 255), SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50)
			draw_text(screen, "Press SPACE to Start", font, (255, 255, 255), SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 10)

			keys = pygame.key.get_pressed()
			if keys[pygame.K_SPACE]:
				game_state = "PLAYING"



		pygame.display.flip()
		dt = clock.tick(60) / 1000
		
	
	


if __name__ == "__main__":
    main()
