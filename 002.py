# The circumference
import math as m
def get_radius(circumference):
  # since we know, $$c = 2\pi r$$

  # $$r = \frac{c}{2\pi}$$

  return circumference / (2 * m.pi)

c1 = 40_000_000 #meters
r1 = get_radius(c1)

c2 = c1+1
r2 = get_radius(c2)

print(f"{round((r2 - r1) * 100, 3)} cm")