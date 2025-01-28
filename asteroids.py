import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Asteroids")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load spaceship image
ship_img = pygame.image.load("ship.png")
ship_img = pygame.transform.scale(ship_img, (40, 40))

class Spaceship:
    def __init__(self):
        self.x, self.y = WIDTH // 2, HEIGHT // 2
        self.angle = 0
        self.speed = 0
        self.vel_x, self.vel_y = 0, 0

    def rotate(self, direction):
        self.angle += direction * 5

    def thrust(self):
        self.vel_x += math.cos(math.radians(self.angle)) * 0.2
        self.vel_y += math.sin(math.radians(self.angle)) * 0.2

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y
        
        # Wrap around screen
        self.x %= WIDTH
        self.y %= HEIGHT

    def draw(self):
        rotated_ship = pygame.transform.rotate(ship_img, -self.angle)
        rect = rotated_ship.get_rect(center=(self.x, self.y))
        screen.blit(rotated_ship, rect.topleft)

class Asteroid:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.vel_x = random.uniform(-2, 2)
        self.vel_y = random.uniform(-2, 2)
        self.size = random.randint(20, 50)

    def move(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.x %= WIDTH
        self.y %= HEIGHT

    def draw(self):
        pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), self.size)

# Game loop
running = True
clock = pygame.time.Clock()
ship = Spaceship()
asteroids = [Asteroid() for _ in range(5)]

while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        ship.rotate(-1)
    if keys[pygame.K_RIGHT]:
        ship.rotate(1)
    if keys[pygame.K_UP]:
        ship.thrust()
    
    ship.move()
    ship.draw()
    
    for asteroid in asteroids:
        asteroid.move()
        asteroid.draw()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
