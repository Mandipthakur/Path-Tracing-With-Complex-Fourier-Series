import pygame
import math

pygame.init()
WIDTH, HEIGHT = 800, 600
time = 0
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fourier Series")
running = True
pastY = []
Signal = [100, 100, 100, -100, -100, -100, 100, 100, 100, -100, -100, -100]

def dft(signal):
    result = []
    N = len(signal)
    for k in range(N):
        re = 0
        im = 0
        for n in range(N):
            phi = (2 * math.pi * k * n) / N
            re += signal[n] * math.cos(phi)
            im -= signal[n] * math.sin(phi)
        re /= N
        im /= N

        amplitude = math.sqrt(re**2 + im**2)
        phase = math.atan2(im, re)

        result.append({
            'frequency': k,
            'amplitude': amplitude,
            'phase': phase
        })
 
    return result

fourierY = dft(Signal)

# # Debug: Print Fourier coefficients
# print("Fourier Coefficients:")
# for i, coeff in enumerate(fourierY):
#     print(f"Freq: {coeff['frequency']}, Amp: {coeff['amplitude']}, Phase: {coeff['phase']}")

def draw():
    global time
    x = 0
    y = 0
    for i in range(len(fourierY)):
        px = x
        py = y
        
        x += radius * math.cos(freq * time + phase + (math.pi)/2)
        y += radius * math.sin(freq * time + phase + (math.pi)/2) 
        pygame.draw.circle(screen, (255, 0, 0), (int(px) + 200, int(py) + 200), int(radius), width=1)
        pygame.draw.line(screen, (255, 255, 255), (int(px) + 200, int(py) + 200), (int(x) + 200, int(y) + 200), 3)
    
    # Debug: Print current x and y values
    print(f"x: {x}, y: {y}")
    
    pastY.append(int(y))
    for i in range(len(pastY)):
        pygame.draw.circle(screen, (255, 255, 255), (int(i / 5) + 300, pastY[i] + 200), 1)
    if len(pastY) > 1:
        pygame.draw.line(screen, (255, 255, 255), (int(x) + 200, int(y) + 200), (int(len(pastY) / 5) + 300, pastY[-1] + 200), 3)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    dt = (2* math.pi) / len(fourierY)
    time += dt  # Increment time for animation
    draw()
    pygame.display.flip()

pygame.quit()
