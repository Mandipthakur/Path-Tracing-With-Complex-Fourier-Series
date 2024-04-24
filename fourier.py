import pygame
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
time = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fourier Series")
running = True
pastY = []
def draw():
    x = 0
    y = 0
    for i in range (0,20):
        px = x
        py = y
        n = i * 2 + 1
        radius = 50 * (4/ (n * math.pi))
        x +=  radius * math.cos( n * time )
        y +=  radius * math.sin( n * time )
        pygame.draw.circle(screen, (255, 0, 0), (px + 200,py + 200),radius, width=1)
        # pygame.draw.circle(screen, (255, 0, 0), (int(x) + 200, int(y) + 200), 10)  # Draw small circle
        pygame.draw.line(screen, (255,255,255), (px + 200 , py + 200), (x + 200 , y + 200), 3)
    pastY.append(int(y))  
    for i in range(len(pastY)):
        pygame.draw.circle(screen, (255, 255, 255), (i/ 5 + 300 , pastY[i] + 200 ), 1)
    pygame.draw.line(screen, (255,255,255), (x + 200, y + 200), (i / 5 + 300 , pastY[i] + 200 ), 3)

            
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    
    time += 0.01  # Increment time for animation
    draw()
    pygame.display.flip()

pygame.quit()
