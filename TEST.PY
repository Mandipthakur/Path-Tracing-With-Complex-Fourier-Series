import math
import pygame as pg


def init():
    """Initialization calls"""
    pg.init()
    screen = pg.display.set_mode((800, 600), flags=pg.RESIZABLE)
    return screen, pg.time.Clock()


def coords(x, y):
    """Used to translate the coordinates origin"""
    return 300 + x, 300 + y


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
Signal = []
for  i in range(100):
    Signal.append(i)
    fourierY = dft(Signal)
# Signal = [100, 100, 100, -100, -100, -100, 100, 100, 100, -100, -100, -100]
    

def mainloop(screen: pg.Surface, main_clock: pg.time.Clock):
    background_color = "black"
    run = True

    time = 0  # angle for polar-to-cartesian conversion
    r = 100
    wave = []
    circles = 10
    circle_color = (100, 100, 100)

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    circles += 1
                elif event.key == pg.K_DOWN:
                    circles -= 1

        screen.fill(background_color)

        x, y = 0, 0
        for i in range(0, circles):
            previous_x = x
            previous_y = y
            freq = fourierY[i]['frequency']
            radius = fourierY[i]['amplitude']
            phase = fourierY[i]['phase']
            
            
            x += radius * math.cos(freq * time + phase + (math.pi)/2)
            y += radius * math.sin(freq * time + phase + (math.pi)/2)

            pg.draw.line(screen, "white", coords(previous_x, previous_y), coords(x, y))
            pg.draw.circle(screen, circle_color,
                           coords(previous_x, previous_y), radius=radius, width=1)

        wave.insert(0, y)
        if len(wave) > 2:
            pg.draw.aalines(screen, pg.Color("white"), False,
                            [coords(200 + i, wave[i]) for i in range(len(wave))], 1 )

        pg.draw.line(screen, pg.Color("white"), coords(x, y), coords(200, wave[0]), 1)

        dt = (2* math.pi) / len(fourierY)
        time += dt  # Increment time for animation
        pg.display.flip()
        main_clock.tick(60)


def main():
    mainloop(*init())
    pg.quit()


if __name__ == "__main__":
    main()