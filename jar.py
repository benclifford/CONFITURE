import neopixel
import board
import random
import time
import math

pixels = neopixel.NeoPixel(board.GP2, 49, auto_write=False)


def contr1():
    pixels.fill( (64, 2, 16) )
    for n in range(0, 24):
        pixels[n*2] = (2, 64, 16)
    pixels.show()

def contr2():
  while True:
    pixels.fill( (0,0,0) )
    for n in range(0, 49):
      if random.random() > 0.5:
        pixels[n] = (2, 64, 16)
      else:
        pixels[n] = (64, 2, 16)
            
    pixels.show()
    time.sleep(1)
    yield

def flame1():
    while True:
        pixels.fill( (0,0,0) )
        for n in range(0, 49):
            if random.random() > (48-n)/48.0:
                yc  = int(255.0 * gamma(n/48.0))
                pixels[n] = (255, yc, 0)
            # else leave blank
        pixels.show()
        time.sleep(1)

def flame2():

    c = 0
    heat = [0] * 49

    start_heat = 1.0

    while True:

        heat[0] = start_heat

        new_heat = [0] * 49

        for n in range(0,49):
            k = 0.30 + random.random() * 0.03
            k2 = 0.10 + random.random() * 0.03

            new_heat[n] += heat[n] * (0.3 + random.random() * 0.2)

            if n <= 47:
                new_heat[n+1] += heat[n] * k

            if n <= 44:
                new_heat[n+4] += heat[n] * k2

        heat = new_heat


        for n in range(0,49):
            h = heat[n]


            if h < 0.001:
                 r = 0
                 g = 0
                 b = 0
            elif h < 0.33:
                 r =  int(heat[n] / 0.33 * 255.0)
                 g = 0
                 b = 0
            elif h < 0.66:
                 r = 255
                 g =  int((heat[n] - 0.33) / 0.33 * 255.0)
                 b = 0
            elif h < 0.99:
                 r = 255
                 g = 255
                 b =  int((heat[n] - 0.99) / 0.33 * 255.0)
            else:
                 r = 255
                 g = 255
                 b = 255

            pixels[48-n] = (r,g,b)

        pixels.show()
        time.sleep(0.1)
        c += 1


def flame3():

    c = 0
    heat = [0] * 49

    start_heat = 1.0

    while True:

        if random.random() < 0.1:
            hpix = random.randrange(0,15)
            heat[hpix] = max(0.0, min(1.0, heat[hpix] + random.random() * 0.7 - 0.1))

        new_heat = [0] * 49

        for n in range(0,48):

            t = 0
            if n > 0:
                t += heat[n-1]

            if n < 47:
                t += heat[n+1]

            t += heat[n]

            new_heat[n] = t / 3.0

        heat = new_heat


        for n in range(0,49):
            h = heat[n]


            if h < 0.001:
                 r = 0
                 g = 0
                 b = 0
            elif h < 0.33:
                 r =  int(gamma(heat[n] / 0.33) * 255.0)
                 g = 0
                 b = 0
            elif h < 0.66:
                 r = 255
                 g =  int(gamma((heat[n] - 0.33) / 0.33) * 255.0)
                 b = 0
            elif h < 0.99:
                 r = 255
                 g = 255
                 b =  int(gamma((heat[n] - 0.66) / 0.33) * 255.0)
            else:
                 r = 255
                 g = 255
                 b = 255

            pixels[48-n] = (r,g,b)

        pixels.show()
        time.sleep(0.05)
        c += 1



def phase1():
    """show a white wave phasing through the LEDs over the course of 1 second"""
    def norm(x): # normalise -1 .. 1 for display
        pos = 0.5 + 0.5 * x
        gp = gamma(pos)
        byterange = 255.0 * gp
        return int(byterange)

    c = 0

    delay = 0.01
    step = 6.28 * 0.01
    while True:
        pixels.fill( (0,0,0) )
        for n in range(0, 49):
            p_phase = (n / 49.0) * 6.28
            r = norm(math.sin(c + p_phase))
            g = norm(math.sin(c + p_phase))
            b = norm(math.sin(c + p_phase))
            pixels[n] = (r, g, b)
        pixels.show()
        time.sleep(delay)
        c += step

def phase2():
    def norm(x): # normalise -1 .. 1 for display
        pos = 0.5 + 0.5 * x
        gp = gamma(pos)
        byterange = 255.0 * gp
        return int(byterange)

    c = 0

    delay = 0.01
    step = 6.28 * 0.01
    while True:
        pixels.fill( (0,0,0) )
        for n in range(0, 49):
            p_phase = (n / 49.0) * 6.28
            r = norm(math.sin(c + p_phase + 0))
            g = norm(math.sin(c + p_phase + 6.28/3.0))
            b = norm(math.sin(c + p_phase + 6.28/3.0*2.0))
            pixels[n] = (r, g, b)
        pixels.show()
        time.sleep(delay)
        c += step


def phase3():
    def norm(x): # normalise -1 .. 1 for display
        pos = 0.5 + 0.5 * x
        gp = gamma(pos)
        byterange = 255.0 * gp
        return int(byterange)

    c = 0
    d = 0

    delay = 0.01
    c_step = 6.28 * 0.01
    d_step = 6.28 * 0.001
    while True:
        pixels.fill( (0,0,0) )
        # mag = 0.5 + 0.5 * math.sin(d + p_phase)
        r_mag = 0.5 + 0.5 * math.sin(d)
        g_mag = 0.5 + 0.5 * math.sin(d + 6.28/3.0)
        b_mag = 0.5 + 0.5 * math.sin(d + 6.28/2.0)
        for n in range(0, 49):
            p_phase = (n / 49.0) * 6.28
            r = norm(r_mag * math.sin(c + p_phase + 0))
            g = norm(g_mag * math.sin(c + p_phase + 6.28/3.0))
            b = norm(b_mag * math.sin(c + p_phase + 6.28/3.0*2.0))
            pixels[n] = (r, g, b)
        pixels.show()
        time.sleep(delay)
        c += c_step
        d += d_step

def phase4():
    c = 0

    delay = 0.01
    step = 6.28 * 0.01
    while True:
        pixels.fill( (0,0,0) )
        for n in range(0, 49):
            p_phase = (n / 49.0) * 6.28
            r = norm(math.sin(c + p_phase + 0))
            g = norm(math.sin(c * 1.07 + p_phase + 6.28/3.0))
            b = norm(math.sin(c * (-1.11) + p_phase + 6.28/3.0*2.0))
            pixels[n] = (r, g, b)
        pixels.show()
        time.sleep(delay)
        yield
        c += step

def phase5():
    def gamma(x,g):
        return math.pow(x,g)

    def norm(x,g ): # normalise -1 .. 1 for display
        pos = 0.5 + 0.5 * x
        gp = gamma(pos,g)
        byterange = 255.0 * gp
        return int(byterange)

    c = 0

    delay = 0.05
    step = 0.1
    while True:
        ga = 0.5 + c % 4
        # print(f"ga = {ga}")
        pixels.fill( (0,0,0) )
        for n in range(0, 49):
            p_phase = (n / 49.0) * 6.28
            r = norm(math.sin(p_phase + 0), ga)
            g = norm(math.sin(p_phase + 6.28/3.0), ga)
            b = norm(math.sin(p_phase + 6.28/3.0*2.0), ga)
            pixels[n] = (r, g, b)
        pixels.show()
        time.sleep(delay)
        c += step





def strobe1():
    def pulse():
        pixels.fill((255, 64, 0))
        pixels.show()
        time.sleep(0.050)
        pixels.fill((0, 0, 0))
        pixels.show()
        time.sleep(0.150)
    while True:
        pulse()
        pulse()
        pulse()
        pulse()
        time.sleep(2)

def strobe2():
    def top_fill(v):
        for led in range(0,16):
            pixels[led] = v

    def pulse():
        top_fill((255, 64, 0))
        pixels.show()
        time.sleep(0.050)
        top_fill((0, 0, 0))
        pixels.show()
        time.sleep(0.150)


    pixels.fill( (0,0,0) )
    for led in range(32,49):
        pixels[led] = (255, 0, 0)

    while True:
        pulse()
        pulse()
        pulse()
        pulse()
        time.sleep(1)


def rgb1():
    for n in range(0,49):
        if n%3 == 0:
            pixels[n] = (255,0,0)
        elif n%3 == 1:
            pixels[n] = (0,255,0)
        else:
            pixels[n] = (0,0,255)

    pixels.show()

def primaryswitcher1():

    pixels.fill( (0,0,0) )
    pixels.show()

    hue = 0

    while True:
        # hue can move to anywhere between 0.2 and 0.8 (= 1 - 0.2)
        # around the circle
        hue = (hue + 0.2 + random.random() * 0.6) % 1.0
        col = hue_saturated(hue)
        for n in range(0,49):
            pixels[n] = col
            pixels.show()
            time.sleep(0.01) # about half a second to fill
            yield

        for n in range(0,200):
            time.sleep(0.01)
            yield

        for n in range(0,49):
            pixels[48-n] = (0,0,0)
            pixels.show()
            time.sleep(0.01) # about half a second to fill
            yield


def primaryswitcher2():

    pixels.fill( (0,0,0) )
    pixels.show()

    hue = 0

    while True:
        # hue can move to anywhere between 0.2 and 0.8 (= 1 - 0.2)
        # around the circle
        hue = (hue + 0.25 + random.random() * 0.5) % 1.0
        col = hue_saturated(hue)
        for n in range(0,49):
            pixels[n] = col
            pixels.show()
            time.sleep(0.005)
            yield

def gamma(x):
    return math.pow(x, 2.3)

def hue_saturated(hue):
    angle = math.pi * 2.0 * hue
    r = math.sin(angle)
    g = math.sin(angle + math.pi * 2.0 / 3.0)
    b = math.sin(angle - math.pi * 2.0 / 3.0)
    return (norm(r), norm(g), norm(b))

def norm(x): # normalise -1 .. 1 and gamma correct for display 
    pos = 0.5 + 0.5 * x
    gp = gamma(pos)
    byterange = 255.0 * gp
    return int(byterange)
