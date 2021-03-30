import board
import rotaryio

import jar

print("CONFITURE: jam jar executive")

rotary_encoder = rotaryio.IncrementalEncoder(board.GP3, board.GP4)

modes = [jar.primaryswitcher1, jar.phase4, jar.primaryswitcher2, jar.contr2, jar.phase1, jar.rgb1, jar.fountain1]

def main_driver():
  n = 0
  current_mode = modes[0]()
  current_mode_pos = 0
  while True:
    # print(f"driving, iteration {n}, encoder is {rotary_encoder.position}")

    if rotary_encoder.position != current_mode_pos:
      print("Changing mode")
      current_mode_pos = rotary_encoder.position
      new_mode = current_mode_pos % len(modes)
      current_mode = modes[new_mode]()

    current_mode.__next__()
    n += 1

if __name__ == "__main__":
  main_driver()
