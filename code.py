import board
import rotaryio

import jar

print("CONFITURE: jam jar executive")

current_mode = jar.primaryswitcher1()
current_mode_pos = 0

rotary_encoder = rotaryio.IncrementalEncoder(board.GP3, board.GP4)

n = 0

modes = [jar.primaryswitcher1, jar.phase4, jar.primaryswitcher2, jar.contr2, jar.phase1]

while True:
  print(f"driving, iteration {n}, encoder is {rotary_encoder.position}")

  if rotary_encoder.position != current_mode_pos:
      print("Changing mode")
      current_mode_pos = rotary_encoder.position
      new_mode = current_mode_pos % len(modes)
      current_mode = modes[new_mode]()

  current_mode.__next__()
  n += 1
