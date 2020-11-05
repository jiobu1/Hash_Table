import hashlib
import random

def hash_function(key):
    return int(hashlib.md5(str(key).encode()).hexdigest()[-8:],16) & 0xffffffff


def how_many_before_collision(buckets, loops):
    for i in range(loops):
        tries = 0
        tried = set()

        while True:
            random_key = random.random()

            index = hash_function(random_key) % buckets

            if index not in tried:
                tried.add(index)
                tries += 1

            else:
                break

        print(f"{buckets} buckets, {tries} hashes before collision, ({tries / buckets * 100}% full)")

how_many_before_collision(32768, 10)

"""
32768 buckets, 108 hashes before collision, (0.32958984375% full)
32768 buckets, 489 hashes before collision, (1.4923095703125% full)
32768 buckets, 126 hashes before collision, (0.384521484375% full)
32768 buckets, 306 hashes before collision, (0.933837890625% full)
32768 buckets, 109 hashes before collision, (0.3326416015625% full)
32768 buckets, 23 hashes before collision, (0.0701904296875% full) # only 7% before collision occurred
32768 buckets, 266 hashes before collision, (0.811767578125% full)
32768 buckets, 175 hashes before collision, (0.5340576171875% full)
32768 buckets, 350 hashes before collision, (1.068115234375% full)
32768 buckets, 94 hashes before collision, (0.286865234375% full)

birthday paradox - only need 16 people in a room before someone has the same birthday as you(-year)
"""