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

static_modes = [jar.rgb1,
                partial(jar.solid, 255, 0, 0),
                partial(jar.solid, 128, 128, 0),
                partial(jar.solid, 0, 255, 0),
                partial(jar.solid, 0, 128, 128),
                partial(jar.solid, 0, 0, 255),
                partial(jar.solid, 128, 0, 128),
                jar.static_random,
                jar.static_saturated_random
               ]

dynamic_modes = [jar.pixphase1, jar.huespin6, jar.huespin5, jar.huespin4, jar.huespin3, jar.huespin2, jar.rainbow1, jar.drip1, jar.huespin1, jar.centre1, jar.vert1, jar.vert2, jar.threepart1, jar.primaryswitcher1, jar.phase4, jar.primaryswitcher2, jar.contr2, jar.phase1, jar.fountain1, jar.contr3]

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

    current_mode.__next__()
    n += 1

if __name__ == "__main__":
  main_driver()
