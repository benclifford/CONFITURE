import neopixel
import board
import random
import time
import math

import configuration

pixels = neopixel.NeoPixel(configuration.neopixel_pin, configuration.num_leds, auto_write=False)

tau = math.pi * 2.0

def nightlight():
  for n in range(0, configuration.num_leds):
    pixels[n] = (1,0,0)

  while True:
    pixels.show()
    yield 0.1


def contrasts(phase):
  tri = tau / 3.0
  p_phase = phase * tau
  p2_phase = (phase + 0.5) * tau
  r = norm(math.sin(p_phase + tri))
  g = norm(math.sin(p_phase - tri))
  b = norm(math.sin(p_phase))

  r2 = norm(math.sin(p2_phase + tri))
  g2 = norm(math.sin(p2_phase - tri))
  b2 = norm(math.sin(p2_phase))

  for n in range(0, configuration.num_leds):
    if n % 2 == 0:
      pixels[n] = (r,g,b)
    else:
      pixels[n] = (r2,g2,b2)

  while True:
    pixels.show()
    yield 0.1



def solid_saturated(phase):
  tri = tau / 3.0
  p_phase = phase * tau
  r = norm(math.sin(p_phase + tri))
  g = norm(math.sin(p_phase - tri))
  b = norm(math.sin(p_phase))

  
  for n in range(0, configuration.num_leds):
    pixels[n] = (r,g,b)

  while True:
    pixels.show()
    yield 0.1

def static_random():
  for n in range(0, configuration.num_leds):
    r = norm2(2.0 * random.random())
    g = norm2(2.0 * random.random())
    b = norm2(2.0 * random.random())
    pixels[n] = (r,g,b)
  while True:
    pixels.show()
    yield 0.1

def static_saturated_random():
  for n in range(0, configuration.num_leds):
    tri = tau / 3.0
    p_phase = random.random() * tau
    r = norm(math.sin(p_phase + tri))
    g = norm(math.sin(p_phase - tri))
    b = norm(math.sin(p_phase))
    pixels[n] = (r,g,b)
  while True:
    pixels.show()
    yield 0.1

def static_saturated_rainbow():
  for n in range(0, configuration.num_leds):
    tri = tau / 3.0
    frac = float(n) / float(configuration.num_leds)
    p_phase = frac * tau
    r = norm(math.sin(p_phase + tri))
    g = norm(math.sin(p_phase - tri))
    b = norm(math.sin(p_phase))
    pixels[n] = (r,g,b)
  while True:
    pixels.show()
    yield 0.1


def static_saturated_magnified_rainbow(p_off):

  for n in range(0, configuration.num_leds):
    tri = tau / 3.0
    frac = float(n) / float(configuration.num_leds)
    p_phase = (frac / 3.0 + p_off) * tau
    r = norm(math.sin(p_phase + tri))
    g = norm(math.sin(p_phase - tri))
    b = norm(math.sin(p_phase))
    pixels[n] = (r,g,b)
  while True:
    pixels.show()
    yield 0.1



def static_white_dither(frac):
  pixels.fill( (0,0,0) )

  intensity = 0.0

  for p in range(0, configuration.num_leds):
    intensity = intensity + frac

    if intensity > 0.5:
      pixels[p] = (255,255,255)
      intensity = intensity - 1.0

  while True:
    pixels.show()
    yield 0.1


def pixphase1():
  phases = [0] * configuration.num_leds 
  phase_shifts = [0.01] * configuration.num_leds
  for n in range(0,configuration.num_leds):
    phases[n] = random.random()
    phase_shifts[n] += random.random() * 0.01

  while True:
    for n in range(0, configuration.num_leds):
      p_phase = phases[n] * tau
      r = norm(math.sin(p_phase))
      g = int(  0.3 * norm(     math.sin(p_phase)   ))
      b = 0
      pixels[n] = (r, g, b)

      phases[n] = (phases[n] + phase_shifts[n]) % 1.0
    pixels.show()
    yield 0.02
     


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
    base = (base + 1) % 6
    yield 0.1
    


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
      yield 0.1

    for n in range(3,46):
      pixels[n] = contr_rgb
      pixels.show()
      yield 0.01
      pixels[n] = (0,0,0)
      pixels.show()


def huespin1():
  hue = random.random()
  while True:
    rgb = hue_saturated(hue)
    pixels.fill(rgb)
    pixels.show()

    hue = (hue + 0.03) % 1.0
    yield 0.03


def huespin2():
  pixels.fill( (0,0,0) )
  hue = random.random()
  while True:
    n = random.randint(0, configuration.num_leds - 1)
    rgb = hue_saturated((hue + random.random() * 0.3) % 1.0)
    pixels[n] = rgb
    pixels.show()
    pixels[n] = (0,0,0)
    yield 0.01

    hue = (hue + 0.001) % 1.0


def huespin3():
  print("huespin3")
  pixels.fill( (0,0,0) )
  hue = random.random()
  while True:

    for n in range(0,configuration.num_leds):
      (r,g,b) = pixels[n]
      pixels[n] = (r * 2/3, g * 2/3, b * 2/3)

    n = random.randint(0,configuration.num_leds - 1)
    rgb = hue_saturated((hue + random.random() * 0.3) % 1.0)
    pixels[n] = rgb
    pixels.show()
    # pixels[n] = (0,0,0)
    yield 0.1

    hue = (hue + 0.01) % 1.0


def huespin4():
  hue = random.random()
  while True:
    hue = (hue + 0.2 + random.random() * 0.5)
    for brightness in range(0,10):
        rgb = hue_saturated(hue, v=brightness/10.0)
        pixels.fill(rgb)
        pixels.show()
        yield 0.03
    for brightness in range(10,-1,-1):
        rgb = hue_saturated(hue, v=brightness/10.0)
        pixels.fill(rgb)
        pixels.show()
        yield 0.03

    for n in range(0,9):
      yield 0.1


def huespin5():
  hue = random.random()
  while True:
    hue = (hue + 0.2 + random.random() * 0.5)
    for brightness in range(0,10):
        rgb = hue_saturated2(hue, v = brightness / 10.0)
        pixels.fill(rgb)
        pixels.show()
        yield 0.03
    for brightness in range(10,-1,-1):
        rgb = hue_saturated2(hue, v = brightness / 10.0)
        pixels.fill(rgb)
        pixels.show()
        yield 0.03

    for n in range(0,9):
      yield 0.1


def huespin5():
  hue = random.random()
  while True:
    hue = (hue + 0.2 + random.random() * 0.5)
    rgb = hue_saturated2(hue)
    for n in range(0,configuration.num_leds):
        pixels[n] = rgb
        pixels.show()
        yield 0.03
    for brightness in range(10,-1,-1):
        rgb = hue_saturated2(hue, v = brightness / 10.0)
        pixels.fill(rgb)
        pixels.show()
        yield 0.03

    yield


def huespin6():
  hue = random.random()
  while True:
    for n in range(0,configuration.num_leds):
      rgb = hue_saturated2(hue + random.random() * 0.25, v = random.random() * 0.5 + 0.5)
      pixels[n] = rgb
    pixels.show()

    hue = (hue + 0.05) % 1.0
    yield 0.05



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
    yield 0.02


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

    hue = (hue + 0.01) % 1.0

    for n in range(0,9):
      yield 0.1


def contr3():
  hue = random.random()
  while True:
    col = hue_saturated(hue)
    contr = hue_saturated((hue + 0.5) % 1)
    pixel = random.randint(0,configuration.num_leds - 1)
    state = random.randint(0,3)

    if state == 0:
        pixels[pixel] = col
    elif state == 1:
        pixels[pixel] = contr
    else: # all other cases, off
        pixels[pixel] = (0, 0, 0)
            
    pixels.show()

    hue = (hue + 0.0001) % 1.0
    yield 0.01


def phase1():
    """show a white wave phasing through the LEDs over the course of 1 second"""
    def norm(x): # normalise -1 .. 1 for display
        pos = 0.5 + 0.5 * x
        gp = gamma(pos)
        byterange = 255.0 * gp
        return int(byterange)

    c = 0

    delay = 0.01
    step = tau * 0.01
    while True:
        pixels.fill( (0,0,0) )
        for n in range(0, configuration.num_leds):
            p_phase = (n / float(configuration.num_leds)) * tau
            r = norm(math.sin(c + p_phase))
            g = norm(math.sin(c + p_phase))
            b = norm(math.sin(c + p_phase))
            pixels[n] = (r, g, b)
        pixels.show()
        c += step
        yield delay

def phase2():
    def norm(x): # normalise -1 .. 1 for display
        pos = 0.5 + 0.5 * x
        gp = gamma(pos)
        byterange = 255.0 * gp
        return int(byterange)

    c = 0

    delay = 0.01
    step = tau * 0.01
    while True:
        pixels.fill( (0,0,0) )
        for n in range(0, configuration.num_leds):
            p_phase = (n / float(configuration.num_leds)) * tau
            r = norm(math.sin(c + p_phase + 0))
            g = norm(math.sin(c + p_phase + tau/3.0))
            b = norm(math.sin(c + p_phase + tau/3.0*2.0))
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
    c_step = tau * 0.01
    d_step = tau * 0.001
    while True:
        pixels.fill( (0,0,0) )
        # mag = 0.5 + 0.5 * math.sin(d + p_phase)
        r_mag = 0.5 + 0.5 * math.sin(d)
        g_mag = 0.5 + 0.5 * math.sin(d + tau/3.0)
        b_mag = 0.5 + 0.5 * math.sin(d + tau/2.0)
        for n in range(0, configuration.num_leds):
            p_phase = (n / float(configuration.num_leds)) * tau
            r = norm(r_mag * math.sin(c + p_phase + 0))
            g = norm(g_mag * math.sin(c + p_phase + tau/3.0))
            b = norm(b_mag * math.sin(c + p_phase + tau/3.0*2.0))
            pixels[n] = (r, g, b)
        pixels.show()
        time.sleep(delay)
        c += c_step
        d += d_step

def phase4():
    c = 0

    delay = 0.01
    step = tau * 0.01
    while True:
        pixels.fill( (0,0,0) )
        for n in range(0, configuration.num_leds):
            p_phase = (n / float(configuration.num_leds)) * tau
            r = norm(math.sin(c + p_phase + 0))
            g = norm(math.sin(c * 1.07 + p_phase + tau/3.0))
            b = norm(math.sin(c * (-1.11) + p_phase + tau/3.0*2.0))
            pixels[n] = (r, g, b)
        pixels.show()
        yield delay
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
            p_phase = (n / float(configuration.num_leds)) * tau
            r = norm(math.sin(p_phase + 0), ga)
            g = norm(math.sin(p_phase + tau/3.0), ga)
            b = norm(math.sin(p_phase + tau/3.0*2.0), ga)
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
        yield 0.1

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
            yield 0.01  # about half a second to fill

        t = time.time()
        while time.time() - t < 2:
            yield 0.2

        for n in range(0,configuration.num_leds):
            pixels[configuration.num_leds - 1-n] = (0,0,0)
            pixels.show()
            yield 0.01


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
            yield 0.005


def fountain1():
    pix = [None] * configuration.num_leds
    pixels.fill( (0,0,0) )
    pixels.show()

    while True:
        if random.randint(0,4) == 0:
            pix[configuration.num_leds - 1] = (int(math.pow(2, random.randint(0,7))),
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
        yield 0.1


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
        yield 0.3
        for p in range(base, base+16):
            pixels[p] = (0,0,0)
        pixels.show()
        yield 0


def vert1():
    pixels.fill( (0,0,0) )
    pixels.show()

    while True:

        base = random.randint(0,configuration.num_leds)

        rgb = hue_saturated(base / float(configuration.num_leds))

        for p in range(base, base+8):
            pixels[p % configuration.num_leds] = rgb

        pixels.show()
        yield 0.1
        pixels.fill( (0,0,0) )
        pixels.show()


def vert2():
    base = random.randint(0,configuration.num_leds)

    while True:

        pixels.fill( (0,0,0) )
        base = (base + random.randint(-1,1)) % configuration.num_leds

        rgb = hue_saturated(base / float(configuration.num_leds))

        for p in range(base, base+8):
            pixels[p % configuration.num_leds] = rgb

        pixels.show()
        yield 0.01


# given a phase return the relevant colour
# phase will go from 0..29
def firefly_green_red(phase):
  if phase < 10:
    return (0,0,0)
  elif phase <= 20:
    return (0,255,0)
  elif phase <= 25:
    return (64,64,0)
  elif phase <= 26:
    return (32,16,0)
  elif phase <= 27:
    return (16,4,0)
  elif phase <= 28:
    return (8,0,0)
  elif phase <= 29:
    return (4,0,0)
  else: 
    return (0,0,0)

def firefly_orange_pulse(phase):
  if phase <= 9:
    return (0,0,0)
  elif phase <= 11:
    return (64,16,0)
  elif phase <= 13:
    return (128,32,0)
  elif phase <= 15:
    return (255,64,0)
  elif phase <= 17:
    return (128,32,0)
  elif phase <= 19:
    return (64,16,0)
  else:
    return (0,0,0)

def firefly_blue_blip(phase):
  if phase <= 9:
    return (0,0,0)
  elif phase <= 11:
    return (0,0,255)
  else:
    return (0,0,0)

def firefly_rainbow(phase):

  tri = tau / 3.0
  p_phase = float(phase)/30.0 * tau
  r = norm(math.sin(p_phase + tri))
  g = norm(math.sin(p_phase - tri))
  b = norm(math.sin(p_phase))

  return (r,g,b)
  

def firefly(led_function):

  pixels.fill( (0,0,0) )
  pixels.show()

  phase = [0] * configuration.num_leds
  phase[25] = 10

  ctr = 0

  while True:
    ctr = ctr + 1
    if ctr > 50:
        n = random.randint(0,configuration.num_leds-1)
        if phase[n] < 10:
            phase[n] = 10   # only fire if we're in accumulating mode
        ctr = 0

    # phase is an integer that ticks up:
    # 0 - 10: pixel has observed neighbours have brightness
    # and is accumulating fire
    # 10-30: pixel has fired and is walking through its colour/cooling sequence

    
    # time.sleep(1)
    # print("")
    for n in range(0, configuration.num_leds):
      # print(f"pixel {n}={phase[n]}  ", end='')
      pixels[n] = led_function(phase[n])

      if phase[n] < 10:
        if n >= 1 and phase[n-1] >= 10 and phase[n-1] <= 25: # negative neighbour alive
          phase[n] += 1
        elif n < configuration.num_leds - 1 and phase[n+1] >= 10 and phase[n+1] <= 25: # positive  neighbour alive
          phase[n] += 1
        elif phase[n] > 0:
          phase[n] -= 1  # reduce stored intensity if no stimulus

      elif phase[n] >= 10:  # stepping through the activated sequence

        phase[n] += 1
        if phase[n] > 30:
          phase[n] = 0
    pixels.show()
    yield 0.02

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
