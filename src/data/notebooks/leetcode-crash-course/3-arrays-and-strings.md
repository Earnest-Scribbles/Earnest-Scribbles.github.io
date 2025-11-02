---
title: "Arrays and Strings"
pubDate: 2024-11-16
chapter: 3
draft: false
notebookTitle: "Leetcode - Interview Crash Course"
---
- Technically Arrays cannot be resized but dynamic arrays can and strings are immutable
- Appeding to the list is [amortized $O(1)$](https://stackoverflow.com/questions/33044883/why-is-the-time-complexity-of-pythons-list-append-method-o1)
- The easy way to understand this is that once the size is decided for an array, let say 8 elements, then appending those elements will be $O(1)$, any other element after that will trigger reallocation for additional 8 elements, this reallocation will take time: $O(n)$, the distribution of these elements when amortized per element is $O(n) / n = O(1)$

## Two Pointers
- will have two integers like `i` and `j` or `left` and `right`
- these represent an index of the array or string
> **First method**: Start the pointers at the edges of the input. Move them towards each other until they meet
- Pseudocode for the same:
```java
function fn(arr):
  left = 0
  right = arr.lenght - 1

  while left < right:
    // Do some logic here depending on the problem
    // Do some more logic here to decide on one of the following:
      // 1. left ++
      // 2. right --
      // 3. Both left++ and right--
```
If we keep the work inside the `while` loop at $O(1)$, this technique will have a Time Complexity of $O(n)$
- Example of checking if a string or an array is a palindrome
```python
# Time complexity: O(n), Space complexity: O(1)
def check_if_palindrome(s):
  left = 0
  right = len(s) - 1

  while left < right:
    if s[left] != s[right]:
      return False
    
    left += 1
    right -= 1

  return True
```
- Example of finding a target integer in a sorted array of unique numbers
```python
# Time complexity: O(n), Space complexity: O(1)
def check_for_target(nums, target):
  left = 0
  right = len(nums) - 1

  while left < right:
    curr = nums[left] + nums[right]
    if curr == target:
      return True

    if curr > target:
      right -= 1
    else:
      left += 1
  
  return False
```
- *Flavors*: Having two pointers but starting the pointers at different indices
> **Second method**: Move along both inputs simultaneously until all elements have been checked
- Applicable when the problem has two iterables in the input
- Pseudocode for the same:
```java
function fn(arr1, arr2):
    i = j = 0
    while i < arr1.length AND j < arr2.length:
        // Do some logic here depending on the problem
        // Do some more logic here to decide on one of the following:
        //     1. i++
        //     2. j++
        //     3. Both i++ and j++

    // Step 4: make sure both iterables are exhausted
    // Note that only one of these loops would run
    while i < arr1.length:
        // Do some logic here depending on the problem
        i++

    while j < arr2.length:
        // Do some logic here depending on the problem
        j++
```
If we keep the work inside the `while` loop at $O(1)$, this technique will have a Time Complexity of $O(n + m)$ where `n = arr1.length` and `m = arr2.length`
- Example of combining two sorted arrays which is also sorted
```python
# Time complexity: O(n), Space complexity: O(1) [if we don't count the output as extra space, which we usually don't]
def combine(arr1, arr2):
  # ans is the answer
  ans = []
  i = j = 0

  while i < length(arr1) and j < length(arr2):
    if arr1[i] < arr2[j]:
      ans.append(arr1[i])
      i += 1
    else:
      ans.append(arr2[j]):
      j += 1

  while i < length(arr1):
    ans.append(arr1[i])
    i += 1

  while j < length(arr2):
    ans.append(arr2[j])
    j += 1
  
  return ans
```
- Example of finding if a string $s$ is a subsequence of $t$ while maintaining the relative order of the characters
```python
# Time complexity: O(n), Space complexity: O(1)
def issubsequence(s, t):
  i = j = 0

  while i < length(s) and j < length(t):
    if s[i] == t[j]:
      i += 1
    j += 1

  return i == len(s)
```
- *Flavors*: Having only one input array/string and initializing both pointers at the first index and move both of them forward, Three pointers

## Sliding Window
- Implemented using two pointers
- Subarrays/Window: A contagious section of an array. Elements must be adjacent to each other and in the same order as in the original array. Example - `[1, 2, 3, 4]`. The subarrays for this array are - 
  - `[1]`, `[2]`, `[3]`, `[4]`
  - `[1, 2]`, `[2, 3]`, `[3, 4]`
  - `[1, 2, 3]`, `[2, 3, 4]`
  - `[1, 2, 3, 4]`
- Subarray can be defined by two indices, the start(left bound) and the end(right bound)
- *When to use sliding window?*
  1. The problem will define criteria that make a subarray **valid**. There are 2 components that will make a subarray valid - 
      - **Constraint metric**: Attribute of the subarray. e.g. the sum, the number of unique elements, frequency of a specific element, or any other attribute
      - **Numeric restriction on the constraint metric**: Constraint metric should follow this for a subarray to be valid
  2. The problem will ask to find valid subarrays in some way - 
      - The most common task you will see is finding the best valid subarray. The problem will define what makes a subarray better than another. For example, a problem might ask you to find the longest valid subarray
      - Another common task is finding the number of valid subarrays  
- Example: 
    - Find the longest subarray with a sum less than or equal to k
    - Find the longest substring that has at most one "0"
    - Find the number of subarrays that have a product less than k
- Psuedocode - 
```java
function fn(arr):
    left = 0
    for (int right = 0; right < arr.length; right++):
        // Do some logic to "add" element at arr[right] to window

        while WINDOW_IS_INVALID:
            // Do some logic to "remove" element at arr[left] from window
            left++

        // Do some logic to update the answer
```
- Time complexity: $O(n)$, if the logic in every window is kept to $O(1)$. A sliding window guarantees a maximum of $2n$ window iterations - the right pointer can move $n$ times and the left pointer can move $n$ times
- Example of finding the length of longest subarray whose sum is equal to or less than `k`
```python
# Time complexity: O(n), Space complexity: O(1)
def find_length(nums, k):
    # curr is the current sum of the window
    left = curr = ans = 0
    for right in range(len(nums)):
      curr += nums[right]
      while curr > k:
        curr -= nums[left]
        left += 1
      ans = max(ans, right - left + 1)

    return ans
```
- Example of longest substring that contains only `1` from a binary string `s`
```python
# Time complexity: O(n), Space complexity: O(1)
def find_length(s):
    # curr is the current number of zeros in the window
    left = curr = ans = 0
    for right in range(len(s)):
      if s[right] == "0":
        curr += 1
      while(curr > 1):
        if s[left] == "0":
          curr -= 1
        left += 1
      ans = max(ans, right - left + 1)

    return ans
```
- **Number of subarrays**: Example of number of subarrays where the product of all the elements in the subarray is strictly less than `k`
```python
# Time complexity: O(n), Space complexity: O(1)
def numSubarrayProductLessThanK(nums, k):
  if k <= 1:
    return 0
  
  left = ans = 0
  curr = 1

  for right in range(len(nums)):
    curr *= nums[right]
    while curr >= k:
      curr //= nums[left]
      left += 1
    ans += right - left + 1

  return ans
```
- **Fixed window size**: Problems with a fixed length `k` for a window.
Psudeocode:
```java
function fn(arr, k):
    curr = some data to track the window

    // build the first window
    for (int i = 0; i < k; i++)
        Do something with curr or other variables to build first window

    ans = answer variable, probably equal to curr here depending on the problem
    for (int i = k; i < arr.length; i++)
        // Add arr[i] to window
        // Remove arr[i - k] from window
        // Update ans

    return ans
```
- Example of finding the largest sum of a subarray in an array with a fixed length `k`
```python
# Time complexity: O(n), Space complexity: O(1)
def find_best_subarray(nums, k):
  curr = 0
  for i in range(k):
    curr += nums[i]

  ans = 0
  for i in range(k, len(nums)):
    curr += nums[i] - nums[i - k]
    ans = max(ans, curr)

  return ans
```

## Prefix Sum
- allow to find the sum of the array nin $O(1)$
- form of a preprocessing, store precomputed data before the main logic of an algorithm
- sum of an subarray from `i` to `j`(inclusive) is `prefix[j] - prefix[i - 1]` or `prefix[j] - prefix[i] + nums[i]`
- Psuedocode
```java
// Given an arr num

prefix = [nums[0]]
for (int i = 1; i < nums.length; i++):
  prefix.append(nums[i] + prefix[prefix.length - 1])
```
- Great when a problem *involves sum of a subarray*, Costs $O(n)$ to build but allows future subarray queries to be $O(1)$
- Example of returning an array with boolean values representing the answer of the `queries` where `queries[i] = [x, y]` and an integer `limit` with the sum of the subarray from `x` to `y` is less than the `limit`
```python
# Time complexity: O(n + m), Space complexity: O(n)
def answer_queries(nums, queries, limit):
  prefix = [nums[0]]

  for i in range(1, len(nums)):
    prefix.append(nums[i] + prefix[-1])

  ans = []
  for x, y in queries:
    curr = prefix[y] - prefix[x] + nums[x]
    ans.append(curr < limit)
  
  return ans
```
- Example of number of ways to split an array `nums` into two parts such that the first section has a sum greater than or equal to the second section
```python
# Time complexity: O(n), Space complexity: O(n)
def waysToSplitArray(self, nums: List[int]) -> int:
  n = len(nums)

  prefix = [nums[0]]
  for i in range(1, n):
    prefix.append(nums[i] + prefix[-1])

  ans = 0
  for i in range(n - 1):
    left_section = prefix[i]
    right_section = prefix[-1] - prefix[i]
    if left_section >= right_section:
      ans += 1

  return ans
```
**Optimisation in the above question** - Realise that the prefix array creation is not actually needed as `left_section` itself is storing the prefix sum and `right_section` can be calculated using `total - left_section` as `right_section` always has the section of the array without the `left_section`. This improves the Space complexity to $O(1)$
```python
# Time complexity: O(n), Space complexity: O(1)
def waysToSplitArray(self, nums: List[int]) -> int:
  ans = left_section = 0
  total = sum(nums)

  for i in range(len(nums) - 1):
    left_section += nums[i]
    right_section = total - left_section
    if left_section >= right_section:
      ans += 1

  return ans
```

## Other Common Patterns
- $O(n)$ string building
```python
def build_string(s):
    arr = []
    for c in s:
        arr.append(c)

    return "".join(arr)
```
- Subarrays/Substrings: A contagious section of a string or an array **[Pattern used: Sliding Window or Prefix Sum]**
- Subsequences: set of elements from the array that keeps same relative order but does not have to be contagious **[Pattern used: Two pointers with two inputs or Dynamic programming]**
- Subsets: any set of elements from the array where relative order and elements being besides matter, here you can sort the input which you cannot do with subsequence **[Pattern used: Backtracking]**