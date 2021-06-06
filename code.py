import board
import rotaryio
import digitalio

import time

import jar

from helpers import partial

print("CONFITURE: jam jar executive")

rotary_encoder = rotaryio.IncrementalEncoder(board.GP9, board.GP10)

rotary_button = digitalio.DigitalInOut(board.GP22)
rotary_button.switch_to_input(pull = digitalio.Pull.UP)


def partial_by_range(func, start, end, step):
  l = []
  v = start
  while v < end:
    l.append(partial(func, v))
    v += step
  return l


static_modes = [jar.rgb1,
               jar.static_random,
               jar.static_saturated_random,
               jar.static_saturated_rainbow] + \
               partial_by_range(jar.solid_saturated, 0, 1, 0.04) + \
               partial_by_range(jar.static_white_dither, 0, 1, 0.1)

dynamic_modes = [jar.pixphase1, jar.huespin6, jar.huespin5, jar.huespin4, jar.huespin3, jar.huespin2, jar.rainbow1, jar.drip1, jar.huespin1, jar.centre1, jar.vert1, jar.vert2, jar.threepart1, jar.primaryswitcher1, jar.phase4, jar.primaryswitcher2, jar.contr2, jar.phase1, jar.fountain1, jar.contr3, jar.firefly]

def main_driver():
  n = 0

  modeset = True  # True/False to represent dynamic/static modes
  current_modeset = modeset

  if modeset:
    mode_list = dynamic_modes
  else:
    mode_list = static_modes

  current_mode = mode_list[0]()
  current_mode_pos = 0
  while True:
    if not rotary_button.value:
      modeset = not modeset
      time.sleep(0.1)

    if rotary_encoder.position != current_mode_pos or current_modeset != modeset:
      current_mode_pos = rotary_encoder.position

      if modeset:
        mode_list = dynamic_modes
      else:
        mode_list = static_modes

      current_modeset = modeset

      new_mode = current_mode_pos % len(mode_list)
      print(f"New mode {new_mode}")
      current_mode = mode_list[new_mode]()

    v = current_mode.__next__()

    if v:
      time.sleep(v)

    n += 1

if __name__ == "__main__":
  main_driver()
