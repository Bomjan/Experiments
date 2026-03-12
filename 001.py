# The constant compression

# This is supposed to take in int and return a list of int
def arrange(x):
  return [int("".join(sorted([i for i in str(x)], reverse=k))) for k in [True, False]]

num = int(input("Enter a non-repeating 4-digit number: "))
a, b = arrange(num)
kapretar_constant = 6174
n = 0
while n != kapretar_constant:
  n = a - b
  print(f"{a} - {b} = {n}")
  a, b = arrange(n)
  