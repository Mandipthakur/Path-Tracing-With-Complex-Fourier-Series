import pygame
import math

pygame.init()
WIDTH, HEIGHT = 800, 600  
time = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Pygame Window")
running = True

class Circle:
    def __init__(self, radius, phase, position):
        self.radius = radius
        self.phase = phase
        self.position = position
        self.pastY = []  
       
    def draw(self):
        x = self.radius * math.cos(time) + self.position[0]  
        y = self.radius * math.sin(time) + self.position[1]  
        pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius, width=1)
        pygame.draw.circle(screen, (255, 0, 0), (int(x), int(y)), 10)  # Draw small circle
        pygame.draw.line(screen, (255,255,255), (200, 200), (x, y), 3)
        self.pastY.append(int(y))  # Append current Y position to trace list
        self.pastX.append(int(x))

        for i in range(len(self.pastY)):
            pygame.draw.circle(screen, (255, 255, 255), (i/10+300, self.pastY[i]), 1)
            pygame.draw.line(screen, (255,255,255), (x, y), (i/10+300, y), 3)

circle1 = Circle(70, 0, (200, 200))  

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    circle1.draw()
    time -= 0.01  # Increment time for animation
    pygame.display.flip()

pygame.quit()
