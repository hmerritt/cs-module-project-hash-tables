import math
import random

# Your code here
cache = {}

def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here
    # Check cache
    if f"{x}{y}" in cache:
        return cache[f"{x}{y}"]
    else:
        v = math.pow(x, y)
        v = math.factorial(v)
        v //= (x + y)
        v %= 982451653

        cache[f"{x}{y}"] = v
        return v

# Build cache
print("Building slowfun cache...\n")
for i in range(2, 14):
    for k in range(3, 6):
        cache[f"{i}{k}"] = slowfun(i, k)

# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
