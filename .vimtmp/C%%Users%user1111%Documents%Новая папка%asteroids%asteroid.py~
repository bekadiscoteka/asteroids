from circleshape import *
from constants import *
from logger import *
import random

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)
	
	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
	
	def update(self, dt):
		self.position += self.velocity * dt	
	
	def split(self):
		self.kill()
		if self.radius == ASTEROID_MIN_RADIUS:
			return
		log_event("asteroid_split")

		rand_angle = random.uniform(20, 50)
		
		new_velocity_1 = self.velocity.rotate(rand_angle)
		new_velocity_2 = self.velocity.rotate(-rand_angle)

		split_1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
		split_2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)

		split_1.velocity, split_2.velocity = new_velocity_1 * 1.2, new_velocity_2 * 1.2


