import math
import pygame as pg



def init():
    """Initialization calls"""
    pg.init()
    screen = pg.display.set_mode((800, 600), flags=pg.RESIZABLE)
    return screen, pg.time.Clock()


def coords(x, y, screen):
    """Used to translate the coordinates origin to the center of the screen"""
    return screen.get_width() // 2 + x, screen.get_height() // 2 + y


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
        amplitude = math.sqrt(re ** 2 + im ** 2)
        phase = math.atan2(im, re)

        result.append({
            'frequency': k,
            'amplitude': amplitude,
            'phase': phase
        })

    return sorted(result, key=lambda x: x['amplitude'], reverse=True)


import random

# Number of tuples to generate
num_tuples = 50

# Empty list to store tuples
random_tuples = []

# Generating random (x, y) tuples
for _ in range(num_tuples):
    x = random.uniform(0, 10)  # Replace 0 and 100 with your desired range for x
    y = random.uniform(0, 30)  # Replace 0 and 100 with your desired range for y
    random_tuples.append((x, y))

# Printing the generated tuples
drawing = random_tuples

# Example drawing signal (replace with actual data)
# drawing = [
#    (0, -50), (-20, -30), (20, -30),
#     (30, -10), (-30, -10),
#     (0, 20), (-10, 30), (10, 30),
#     (0, 20), (0, 0)
# ]s

SignalX = [point[0] for point in drawing]
SignalY = [point[1] for point in drawing]

fourierX = dft(SignalX)
fourierY = dft(SignalY)

# scaling_factor = 1.2 # Adjust this factor to scale the epicycles


def epi_cycles(screen, x, y, rotation, fourier, time, color):
    for component in fourier:
        prev_x, prev_y = x, y
        freq = component['frequency']
        radius = component['amplitude'] * 6
        phase = component['phase']
        x += radius * math.cos(freq * time + phase + rotation)
        y += radius * math.sin(freq * time + phase + rotation)

        pg.draw.circle(screen, color, coords(prev_x, prev_y, screen), radius, 1)
        pg.draw.line(screen, (255, 255, 255), coords(prev_x, prev_y, screen), coords(x, y, screen))
    return x, y


def mainloop(screen: pg.Surface, main_clock: pg.time.Clock):
    background_color = "black"
    run = True

    time = 0
    path = []

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        screen.fill(background_color)

        v1x, v1y = epi_cycles(screen, 50, -200, 0, fourierX, time, (255,0,0))
        v2x, v2y = epi_cycles(screen, -300, 100, math.pi / 2, fourierY, time, (0,255,0))

        path.insert(0, (v1x, v2y))
        if len(path) > len(fourierX):
            path.pop()

        for i in range(1, len(path)):
            pg.draw.line(screen, (255, 255, 255), coords(path[i - 1][0], path[i - 1][1], screen), coords(path[i][0], path[i][1], screen))

        pg.draw.line(screen, (255, 255, 255), coords(v1x, v1y, screen), coords(v1x, v2y, screen))
        pg.draw.line(screen, (255, 255, 255), coords(v2x, v2y, screen), coords(v1x, v2y, screen))

        dt = (2 * math.pi) / len(fourierY)
        time += dt

        pg.display.flip()
        main_clock.tick(10)


def main():
    mainloop(*init())
    pg.quit()


if __name__ == "__main__":
    main()
