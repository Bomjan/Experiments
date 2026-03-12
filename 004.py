# Happy numbers

def separate(x):
  # convert to string
  # split in array
  # convert back to integer
  return [int(i) for i in str(x)]

def is_not_repeating(full_list):
    # Set to store value
    history = set()

    # We slide across the list
    for i in range(len(full_list) - 1):
        # 1. Grab the current value
        current_value = full_list[i]

        # 2. Check if we've seen this exact sequence before
        if current_value in history:
            return False
        else:
            # 3. Store it if it's new. It prolly is
            history.add(current_value)
            
    return True

n = 39
c = sum([x**2 for x in separate(n)])
outputs = [c]


while is_not_repeating(outputs):
  c = sum([x**2 for x in separate(c)])
  outputs.append(c)

print(outputs)
if outputs[-1] == 1:
  print(f"{n} is a happy number")
else:
   print("Not a happy number")
