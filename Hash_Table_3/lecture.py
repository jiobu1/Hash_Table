###################################################################################################################
"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Understand:
Find non-duplicate entry in array
[2,2,1] -> 1
[1] -> 1
[2,1,2] ->

Plan:
Iterate through array and find non-duplicate
Use a dictionary to keep track of how many times an item exists in the list
[element: num times it appeared in the list]

Go through dictionary, output key whose value is 1

[2, 2, 1*] -> 1
{2: 2, 1 :1} -> 1


Runtime: O(n)
Space: O(n)
"""
# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dictionary = {}

        for n in nums:
            if n in dictionary:
                dictionary[n] += 1
            else:
                dictionary[n] = 1

        for (key, value) in dictionary.items():
            if value == 1:
                return key

        return -1

from collections import defaultdict

class Solution:
    #[2,1,2] ->
    def singleNumber(self, nums: List[int]) -> int:
        # return reduce(lambda x,y :x ^y, nums)

        dictionary = defaultdict(int)  # {2:2, 1:1}

        for n in nums:
            if n in dictionary:
                dictionary[n] +=1
            else:
                dictionary[n] =1

        for(key, value) in dictionary.items():
            if value == 1:
                return key

        return -1

#########################################################################################################
"""
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

    add(value): Insert a value into the HashSet.
    contains(value) : Return whether the value exists in the HashSet or not.
    remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Understand:
mySet = MyHashSet()
mySet.add(1) // {1}
mySet.add(2) // {1, 2}
mySet.add(1) // {1, 2}

mySet.contains(1) // True
mySet.remove(1)
mySet.contains(1) // False


Plan

Implement a hash table to implement get/add/remove
Use a popular hashing algorithm to map elements into buckets
Solve collisions using chaining
For simplicity we just need to initialize an array of size 10001 and not need to resize

Runtime: O(1)
Space: O(1)
"""


"""
Examples:
MyHashSet hashSet = new MyHashSet();
hashSet.add(1);
hashSet.add(2);
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);
hashSet.contains(2);    // returns true
hashSet.remove(2);
hashSet.contains(2);    // returns false (already removed)
"""

from collection import deque

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.table = [None] * 10001

    def hash_index(self, key):
        return hash(key) % len(self.table)

    def add(self, key: int) -> None:
        hash_index = self.hash_index(key)
        if self.table[hash_index] == None:
            new_list = deque()
            new_list.append(key)
            self.table[hash_index] = new_list
        elif key not in self.table[hash_index]:
            self.table[hash_index].append(key)

    def remove(self, key: int) -> None:
        hash_index = self.hash_index(key)
        if self.table[hash_index] != None:
            try:
                self.table[hash_index].remove(key)
            except:
                pass

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hash_index = self.hash_index(key)
        if self.table[hash_index] != None:
            return key is in self.table[hash_index]
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)