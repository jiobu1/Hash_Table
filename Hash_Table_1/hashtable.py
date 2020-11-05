# hash function

# takes in inputStr and returns a number
def my_hash(inputStr):
    # 'foo' --> [x, y, y]
    sb = inputStr.encode() # the utf-8 bytes for the string
    total = 0
    for b in sb:
        total += b
    return total

print(my_hash('foo'))

#statically sized table for now (can resize)
my_table = [None] * 8
# store key "foo" w/ value "bar"
hash_index = my_hash("foo") % len(my_table)
my_table[hash_index] = "bar" # assigning value bar to key foo
print(f"1: {my_table}")

# get value w/ key "foo"
another_hash_index = my_hash("foo") % len(my_table)
print(f"2: {my_table[another_hash_index]}")

# delete value w/ key "foo"
yet_another_hash_index = my_hash("foo") % len(my_table) #same as above
my_table[yet_another_hash_index] = None # except make it equal to none
print(f"3: {my_table}")

"""
Understand
1. J = "aA", S = "aAAbbbb"
output 3

2. J = "z", S = "ZZ"
output 0

3. J = "z" S = ""
output 0

Plan
brute-force
for each char s in S, see if it's in J
if it is, then increment result else don't increment it

better approach
convert J into a set j
for each char s in S
   if s is in j then increment result
return result
"""

class Solution:
    # J = "aA", S = "aAAbbbb"
    def numJewelsInStones(self, J: str, S: str) -> int:
        j = set(list(J))
        numJewels = 0
        for s in S:
            if s in j:
                numJewels += 1
        return numJewels

# changes runtime complexity to constant time O(1)
# if you leave it as a list it will loop twice and have a quadratic runtime O(n^2)