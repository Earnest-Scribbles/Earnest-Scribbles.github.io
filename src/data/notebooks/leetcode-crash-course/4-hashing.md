---
title: "Hashing"
pubDate: 2024-12-13
chapter: 4
draft: false
notebookTitle: "Leetcode - Interview Crash Course"
---

## Hash Maps
- Uses a hash function which converts any arbitrary input(keys) into an integer that is less than the fixed size set by a programmer. It has an algorithm and modulus which make sures that the value falls under a range of numbers
- hash funtion is combined with an array, it creates a hash map, hash table or dictionary
- arrays map indices to values, hashmaps maps keys to values. The keys should be immutable. Hash maps are unordered which means that the insertion order is not relevant and not remembered
- The following operations are $O(1)$ for a hash map:
  - Add an element and associate it with a value
  - Delete an element if it exists
  - Check if an element exists
- The most important thing to understand is that with arrays we used to have indexes map to values and we needed the index to get the value. Now, with hash map we can store the values as a key to get direct access to the value.
*This helps to keep the main information in the key of a hash map and keep any meta data related to it in the value part*
- Tradeoffs for hash maps:
  - for smaller input sizes, hash maps are slower because of overhead
  - resizing the hash table is more expensive than resizing a dynamic array
  - **Collisions**: Different keys can convert to the same integer while hashing using a hash function, the data can get overriden and lost in the case if not handled. For handling this, **chaining** is a common approach which stores a linked list inside the array with key, value pair and add the new key, value to its tail. Whenever we search for a value using a key, it will traverse the entire linked list and give us the correct value

## Sets
- very similar to Hash map, but does not map the keys to anything
- helpful if we only care about checking if element exists
- They also don't track frequency, that is sets does not store any duplicate

> Storing an array as key is possible in Hash map and Sets. array are mutable, so we convert it to a tuple in python (`tuple(arr)`) which is immutable and then store it as a key.

## Pattern 1: Checking for existence
- Most common application of a hash table is to determine if an element exists in $O(1)$ as array takes $O(n)$ to do this
- Anytime you find your algorithm running `if ... in ...`, then consider using a hash map or set to store elements to have these operations run in $O(1)$
- Example of returing indices of two numbers such that they add up to `target` in an array `nums`
```python
# Time Complexity: O(n), Space Complexity: O(n)
def twoSum(self, nums: List[int], target: int) -> List[int]:
  dic = {}
  for i in range(len(nums)):
    num = nums[i]
    complement = target - num
    if complement in dic:   # This operation is O(1)!
      return [i, dic[complement]]

    dic[num] = i

  return [-1, -1]
```
- Example of returing the first character to appear twice from a string `s`

*Bruteforce solution*
```python
# Time Complexity: O(n^2), Space Complexity: O(1)
def repeatedCharacter(self, s: str) -> str:
  for i in range(len(s)):
    c = s[i]
    for j in range(len(s)):
      if s[j] == c:
        return c

  return ""
```
*Using a set can reduce this to $O(1)$*
```python
# Time Complexity: O(n)
# Space Complexity
# O(m) where m is the number of allowable characters in the input
# O(1) as input can have characters from English Alphabet which is constant 26
def repeatedCharacter(self, s: str) -> str:
  seen = set()
  for c in s:
    if c in seen:
      return c
    seen.add(c)

  return ""
```
- Example of finding all unique elements `x` in `nums` that satisfy the following: `x + 1` is not in `nums`, and `x - 1` it not in `nums`
```python
# Time Complexity: O(n), Space Complexity: O(n)
def find_numbers(nums):
  ans = []
  nums = set(nums)

  for num in nums:
    if (num + 1 not in nums) and (num - 1 not in nums):
      ans.append(num)

  return ans
```

## Pattern 2: Counting