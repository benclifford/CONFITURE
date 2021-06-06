import neopixel
import board
import random
import time
import math

import configuration

pixels = neopixel.NeoPixel(configuration.neopixel_pin, configuration.num_leds, auto_write=False)


def pixphase1():
  phases = [0] * configuration.num_leds 
  phase_shifts = [0.01] * configuration.num_leds
  for n in range(0,configuration.num_leds):
    phases[n] = random.random()
    phase_shifts[n] += random.random() * 0.01

  while True:
    for n in range(0, configuration.num_leds):
      p_phase = phases[n] * 6.28
      r = norm(math.sin(p_phase))
      g = norm(math.sin(p_phase))
      b = norm(math.sin(p_phase))
      pixels[n] = (r, g, b)

      phases[n] = (phases[n] + phase_shifts[n]) % 1.0
    pixels.show()
    time.sleep(0.02)
    yield
     


def rainbow1():

  base = 0
  while True:
    for n in range(0,configuration.num_leds):
      v = 1 + (base + n) % 6 # cycle through 1..6
      if v & 1 == 0:
        r = 255
      else:
        r = 0
      if v & 2 == 0:
        g = 255
      else:
        g = 0
      if v & 4 == 0:
        b = 255
      else:
        b = 0
      pixels[n] = (r, g, b)
    pixels.show()
    time.sleep(0.1)
    base = (base + 1) % 6
    yield
    


def drip1():
  pixels.fill( (0,0,0) )

  hue = random.random()

  while True:

    rgb = hue_saturated(hue)
    contr_rgb = hue_saturated((hue + 0.3) % 1.0)

    for n in range(0, 3):
      pixels[n] = rgb
    
    for n in range(46, configuration.num_leds):
      pixels[n] = rgb

    pixels.show()

    # TODO: interruptible sleep
    for n in range(0,9):
      time.sleep(0.1)
      yield

    for n in range(3,46):
      pixels[n] = contr_rgb
      pixels.show()
      time.sleep(0.01)
      yield
      pixels[n] = (0,0,0)
      pixels.show()


def huespin1():
  hue = random.random()
  while True:
    rgb = hue_saturated(hue)
    pixels.fill(rgb)
    pixels.show()

    hue = (hue + 0.03) % 1.0
    time.sleep(0.03)
    yield


def huespin2():
  pixels.fill( (0,0,0) )
  hue = random.random()
  while True:
    n = random.randint(0,48)
    rgb = hue_saturated((hue + random.random() * 0.3) % 1.0)
    pixels[n] = rgb
    pixels.show()
    pixels[n] = (0,0,0)
    time.sleep(0.01)
    yield

    hue = (hue + 0.001) % 1.0


def huespin3():
  print("huespin3")
  pixels.fill( (0,0,0) )
  hue = random.random()
  while True:

    for n in range(0,configuration.num_leds):
      (r,g,b) = pixels[n]
      pixels[n] = (r * 2/3, g * 2/3, b * 2/3)

    n = random.randint(0,48)
    rgb = hue_saturated((hue + random.random() * 0.3) % 1.0)
    pixels[n] = rgb
    pixels.show()
    # pixels[n] = (0,0,0)
    time.sleep(0.1)
    yield

    hue = (hue + 0.01) % 1.0


def huespin4():
  hue = random.random()
  while True:
    hue = (hue + 0.2 + random.random() * 0.5)
    for brightness in range(0,10):
        rgb = hue_saturated(hue, v=brightness/10.0)
        pixels.fill(rgb)
        pixels.show()
        time.sleep(0.03)
        yield
    for brightness in range(10,-1,-1):
        rgb = hue_saturated(hue, v=brightness/10.0)
        pixels.fill(rgb)
        pixels.show()
        time.sleep(0.03)
        yield

    time.sleep(1)
    yield


def huespin5():
  hue = random.random()
  while True:
    hue = (hue + 0.2 + random.random() * 0.5)
    for brightness in range(0,10):
        rgb = hue_saturated2(hue, v = brightness / 10.0)
        pixels.fill(rgb)
        pixels.show()
        time.sleep(0.03)
        yield
    for brightness in range(10,-1,-1):
        rgb = hue_saturated2(hue, v = brightness / 10.0)
        pixels.fill(rgb)
        pixels.show()
        time.sleep(0.03)
        yield

    time.sleep(1)
    yield


def huespin5():
  hue = random.random()
  while True:
    hue = (hue + 0.2 + random.random() * 0.5)
    rgb = hue_saturated2(hue)
    for n in range(0,configuration.num_leds):
        pixels[n] = rgb
        pixels.show()
        time.sleep(0.03)
        yield
    for brightness in range(10,-1,-1):
        rgb = hue_saturated2(hue, v = brightness / 10.0)
        pixels.fill(rgb)
        pixels.show()
        time.sleep(0.03)
        yield

    yield


def huespin6():
  hue = random.random()
  while True:
    for n in range(0,configuration.num_leds):
      rgb = hue_saturated2(hue + random.random() * 0.25, v = random.random() * 0.5 + 0.5)
      pixels[n] = rgb
    pixels.show()

    hue = (hue + 0.05) % 1.0
    time.sleep(0.05)
    yield



def centre1():
  width = 6
  while True:
    pixels.fill( (0,0,0) )
    for p in range(24 - width, 24 + width):
      pixels[p] = (255, 255, 255)
    pixels.show()

    # TODO: random walk generator
    width += random.randint(-1,1)
    if width > 12:
        width = 12
    if width < 2:
        width = 2
    time.sleep(0.02)
    yield


def contr2():
  hue = 0
  while True:
    col = hue_saturated(hue)
    contr = hue_saturated((hue + 0.5) % 1)
    for n in range(0, configuration.num_leds):
      if random.random() > 0.5:
        pixels[n] = col
      else:
        pixels[n] = contr
            
    pixels.show()
    time.sleep(1)

    hue = (hue + 0.01) % 1.0
    yield

def contr3():
  hue = random.random()
  while True:
    col = hue_saturated(hue)
    contr = hue_saturated((hue + 0.5) % 1)
    pixel = random.randint(0,48)
    state = random.randint(0,3)

    if state == 0:
        pixels[pixel] = col
    elif state == 1:
        pixels[pixel] = contr
    else: # all other cases, off
        pixels[pixel] = (0, 0, 0)
            
    pixels.show()
    time.sleep(0.01)

    hue = (hue + 0.0001) % 1.0
    yield


def flame1():
    while True:
        pixels.fill( (0,0,0) )
        for n in range(0, configuration.num_leds):
            if random.random() > (48-n)/48.0:
                yc  = int(255.0 * gamma(n/48.0))
                pixels[n] = (255, yc, 0)
            # else leave blank
        pixels.show()
        time.sleep(1)

def flame2():

    c = 0
    heat = [0] * configuration.num_leds

    start_heat = 1.0

    while True:

        heat[0] = start_heat

        new_heat = [0] * configuration.num_leds

        for n in range(0,configuration.num_leds):
            k = 0.30 + random.random() * 0.03
            k2 = 0.10 + random.random() * 0.03

            new_heat[n] += heat[n] * (0.3 + random.random() * 0.2)

            if n <= 47:
                new_heat[n+1] += heat[n] * k

            if n <= 44:
                new_heat[n+4] += heat[n] * k2

        heat = new_heat


        for n in range(0,configuration.num_leds):
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
    heat = [0] * configuration.num_leds

    start_heat = 1.0

    while True:

        if random.random() < 0.1:
            hpix = random.randrange(0,15)
            heat[hpix] = max(0.0, min(1.0, heat[hpix] + random.random() * 0.7 - 0.1))

        new_heat = [0] * configuration.num_leds

        for n in range(0,48):

            t = 0
            if n > 0:
                t += heat[n-1]

            if n < 47:
                t += heat[n+1]

            t += heat[n]

            new_heat[n] = t / 3.0

        heat = new_heat


        for n in range(0,configuration.num_leds):
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
        for n in range(0, configuration.num_leds):
            p_phase = (n / float(configuration.num_leds)) * 6.28
            r = norm(math.sin(c + p_phase))
            g = norm(math.sin(c + p_phase))
            b = norm(math.sin(c + p_phase))
            pixels[n] = (r, g, b)
        pixels.show()
        time.sleep(delay)
        c += step
        yield

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
        for n in range(0, configuration.num_leds):
            p_phase = (n / float(configuration.num_leds)) * 6.28
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
        for n in range(0, configuration.num_leds):
            p_phase = (n / float(configuration.num_leds)) * 6.28
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
        for n in range(0, configuration.num_leds):
            p_phase = (n / float(configuration.num_leds)) * 6.28
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
        for n in range(0, configuration.num_leds):
            p_phase = (n / float(configuration.num_leds)) * 6.28
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
    for led in range(32,configuration.num_leds):
        pixels[led] = (255, 0, 0)

    while True:
        pulse()
        pulse()
        pulse()
        pulse()
        time.sleep(1)


def rgb1():
    for n in range(0,configuration.num_leds):
        if n%3 == 0:
            pixels[n] = (255,0,0)
        elif n%3 == 1:
            pixels[n] = (0,255,0)
        else:
            pixels[n] = (0,0,255)

    while True:
        pixels.show()
        time.sleep(0.1)
        yield

def primaryswitcher1():

    pixels.fill( (0,0,0) )
    pixels.show()

    hue = 0

    while True:
        # hue can move to anywhere between 0.2 and 0.8 (= 1 - 0.2)
        # around the circle
        hue = (hue + 0.2 + random.random() * 0.6) % 1.0
        col = hue_saturated(hue)
        for n in range(0,configuration.num_leds):
            pixels[n] = col
            pixels.show()
            time.sleep(0.01) # about half a second to fill
            yield

        t = time.time()
        while time.time() - t < 2:
            time.sleep(0.2)
            yield

        for n in range(0,configuration.num_leds):
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
        for n in range(0,configuration.num_leds):
            pixels[n] = col
            pixels.show()
            time.sleep(0.005)
            yield


def fountain1():
    pix = [None] * configuration.num_leds
    pixels.fill( (0,0,0) )
    pixels.show()

    while True:
        if random.randint(0,4) == 0:
            pix[48] = (int(math.pow(2, random.randint(0,7))),
                       int(math.pow(2, random.randint(0,7))),
                       int(math.pow(2, random.randint(0,7))))
        # print("==")
        for n in range(0, configuration.num_leds):
            d = random.randint(0,2)
            nd = n - d
            k = pix[n]
            pix[n] = None
            if nd >= 0 and pix[nd] is None:
                pix[nd] = k
            elif nd >= 0:  # (and pix[nd] is not None)
                pix[n] = k # put the pixel back unmoved
            # else it falls off the end and we don't set anything

        for n in range(0,configuration.num_leds):
            if pix[n] is None:
                pixels[n] = (0,0,0)
            else:
                pixels[n] = pix[n]
        pixels.show()
        time.sleep(0.1)
        yield


def threepart1():
    pixels.fill( (0,0,0) )
    pixels.show()
    lastrand = -1 # make this into a generator

    while True:

        # TODO: make this into a generator that is almost-rand
        n = random.randint(0,2)
        while n == lastrand: 
            n = random.randint(0,2)
        lastrand = n

        if n == 0:
            base = 0
        elif n == 1:
            base = 16
        else:
            base = 32

        rgb = hue_saturated(n / 3.0)
        for p in range(base, base+16):
            pixels[p] = rgb
        pixels.show()
        time.sleep(0.3)
        for p in range(base, base+16):
            pixels[p] = (0,0,0)
        pixels.show()
        yield


def vert1():
    pixels.fill( (0,0,0) )
    pixels.show()

    while True:

        base = random.randint(0,configuration.num_leds)

        rgb = hue_saturated(base / float(configuration.num_leds))

        for p in range(base, base+8):
            pixels[p % configuration.num_leds] = rgb

        pixels.show()
        time.sleep(0.1)
        pixels.fill( (0,0,0) )
        pixels.show()
        yield


def vert2():
    base = random.randint(0,configuration.num_leds)

    while True:

        pixels.fill( (0,0,0) )
        base = (base + random.randint(-1,1)) % configuration.num_leds

        rgb = hue_saturated(base / float(configuration.num_leds))

        for p in range(base, base+8):
            pixels[p % configuration.num_leds] = rgb

        pixels.show()
        time.sleep(0.01)
        yield


def gamma(x):
    return math.pow(x, 2.3)


def hue_saturated2(hue, v=1.0):
    angle = math.pi * 2.0 * hue
    # rgb range from 0..2
    r = (math.cos(angle) + 1.0) * v
    g = (math.cos(angle + math.pi * 2.0 / 3.0) + 1.0) * v
    b = (math.cos(angle - math.pi * 2.0 / 3.0) + 1.0) * v
    return (norm2(r), norm2(g), norm2(b))

def norm2(x): # normalise 0 .. 2 and gamma correct for display 
    pos = x / 2.0
    gp = gamma(pos)
    byterange = 255.0 * gp
    return int(byterange)

def hue_saturated(hue, v=1.0):
    angle = math.pi * 2.0 * hue
    r = math.cos(angle) * v
    g = math.cos(angle + math.pi * 2.0 / 3.0) * v
    b = math.cos(angle - math.pi * 2.0 / 3.0) * v
    return (norm(r), norm(g), norm(b))

def norm(x): # normalise -1 .. 1 and gamma correct for display 
    pos = 0.5 + 0.5 * x
    gp = gamma(pos)
    byterange = 255.0 * gp
    return int(byterange)
