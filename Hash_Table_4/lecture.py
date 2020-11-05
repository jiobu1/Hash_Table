# """

# # Iterate over repeated searching over a collection-> use hash table

# Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy that Alice has,
# and B[j] is the size of the j-th bar of candy that Bob has. Since they are friends, they would like to
# exchange one candy bar each so that after the exchange, they both have the same total amount of candy.
# (The total amount of candy a person has is the sum of the sizes of candy bars they have.)
# Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange, and ans[1]
# is the size of the candy bar that Bob must exchange. If there are multiple answers, you may return any
# one of them.  It is guaranteed an answer exists.

# Understand:
# Input A = [1,1], B=[2,2]
# Output: [1,2]

# Example 1:
# A = [1] B = [2,3]
# Output [1,3] --> A = [3], B = [2,1]

# Example 2:
# A = [1] B = [1]
# [1,1]

# Plan
# For every candy x that Alice gives out, she expects a candy y from Bob: sum(alice) - x + y
# for every candy y that bob gives out, he expects a candy x from Alice: sum(bob) - y + x
# since we're doing a fair swap, the candies that Alice and Bob has, needs to be equal

# sum(alice) - x + y = sum(bob) - y + x
# - x + y = sum(bob) - sum(alice) - y + x
# y = sum(bob) - sum(alice) - y + 2x
# 2y = (sum(bob) - sum(alice)/2) + x

# make a set out of Bob's candies and see if he has candy y
# try every candy x that Alice has and see if Bob has candy y that satisfies the above equation.

# runtime: O(len(A) + len(B))
# space: O(len(B))
# """

# class Solution:
#     def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
#         bobCandies = set(B) # Bob's candies will grow linearly with len of B
#         bobSum, aliceSum = sum(B), sum(A)
#         for x in A:
#             y = ((bobSum - aliceSum)/2) + x
#             if y in bobCandies:
#                 return [x,y]
#         return []
# #####################################################################################################

# class Solution:
#     """
#     Input: 2
#     Output: 2
#     Fib(2) = Fib(1) + Fib(0) = 1 + 0 = 1

#     Input: 4
#     Output: 3
#     Fib(4) = Fib(3) + Fib(2) = 2 + 1 = 3

#     Input: 5
#     Output: 5
#     Fib(5) = Fib(4) + Fib(3) = 3 + 2 = 5

#     """

#     def fib(self, N:int) -> int:
#         computedValues = {1:1, 0:0}
#         return self.memoizedFib(N, computedValues)

#     def memoizedFib(self, N, computedValues):
#         if N in computedValues:
#             return computedValues[N]
#         computedValues[N] = self.memoizedFib(N-1, computedValues) + self.memoizedFib(N-2, computedValues)
#         return computedValues[N]

# #####################################################################################################
# """
# 70. Climbing Stairs
# Easy

# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:

# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:

# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# Understand
# Find the maximum number of ways to climb stairs, using 1 or 2 steps at a time
# n = 2
# output = 2
# 1. 1 step + 1 step
# 2. 2 steps

# n = 3
# output = 3
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 step
# 3. 2 steps + 1 step

# n = 1
# output = 1

# Plan
# num_ways(n) = num_ways(n-1) + num_ways(n-2)
# """

# def climbStairs(self, n: int) -> int:
#     computedValues = {2:2, 1:1, 0:0}
#     return self.climbStairs(n, computedValues)

# def climbStairsHelper(self, n, computedValues):
#     if n in computedValues:
#         return computedValues[n]
#     computedValues[n] = self.climbStairsHelper(n-1, computedValues) + self.climbStairsHelper(n-2, computedValues)
#     return computedValues[n]

# # bottom up is also called tablulation - dynamic programming

#####################################################################################################
import random
import time

class Server:
    cache = {}

    def processGETRequest(self, url):
        if url in self.cache:
            print(url + " is already in the cache")
            return self.cache(url)
        print(url + " is not cached yet")
        self.cache[url] = self.doExpensiveComputation(url)
        print("caching" + url + "with value" + str(self.cache[url]))

    def processPUTRequest(self, url):
        # update DB with new values
        # evict url from the cache

    def doExpensiveComputation(self, url):
        time.sleep(5)
        return random.randint(0,101)

server = Server()
server.processGETRequest("google.com")
server.processGETRequest("google.com")
server.processGETRequest("facebook.com")