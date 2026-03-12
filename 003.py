# How many draws?

import random

def get_draw():
  draw = 0
  s = 0
  # random.random()

  while s <= 1:
    s += random.random()
    draw += 1

  return draw

total = 0
for _ in range(100000):
  total += get_draw()

print(total/100000)