# similar to caching but using look up table

import math
# 1/ math.sqrt(n)

# building cache ahead of time
inv_sqrt = {}

def build_lookup_table():
    for i in range(1, 1000):
        inv_sqrt[i] = 1 / math.sqrt(i)


def get_inv_sqrt(n):
    # Lazily add things to the lookup table
    if n not in inv_sqrt:
        inv_sqrt[n] = 1 / math.sqrt(n)

    return inv_sqrt[n]

build_lookup_table()

print(get_inv_sqrt(37))
print(get_inv_sqrt(2000))

# fast inverse square root