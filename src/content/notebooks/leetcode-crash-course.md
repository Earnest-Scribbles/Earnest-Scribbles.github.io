---
external: false
title: "Leetcode - Interview Crash Course"
description: "Notes from the course Leetcode - Data structures and algorithms"
image:
  url: "/notebook/hero/DSA.webp"
  alt: "Flow chart for DSA on a note"
pubDate: 2024-11-16
tags: ["notebook", "programming"]
---


## Introduction to big O
- Computational complexity of an algorithm, Time and Space complexity
- Time complexity: amount of time the algorithm needs to run relative to its input size
- Space complexity: amount of memory allocated by the algorithm when run relative to its input size
- Example complexities: $O(n)$, $O(n^2)$, $O(2^n)$, $O(logn)$, $O(n.m)$
- Logarithmic time($O(logn)$): extremely fast
  - Typically, base of the logarithm will be 2, but it doesnt really matter for big $O$
  - $logn$ just means that the input is being reduced by a percentage at every step. eg. Binary search
- Calculating complexities: Time = number of operations, Space = amount of memory relative to the input size
- Rules:
  - Ignore constants, eg. $O(8n) = O(n) = O(n / 500)$
  - consider the complexity as the variables tend to infinity, eg. $O(2^n + n^2 - 500n) = O(2^n)$
- Three cases when talking about complexities - Best case, Worst case, Average case, to represent we generally use Worst case

## Analyzing Time complexity
- The method is to think about **NUMBER OF OPERATIONS** when analyzing Time complexity and think about **ALLOCATION SPACE** for the variables analying Space complexity.
- Time complexity: How many times something is happening?
Example -
```java
// Given an integer array "arr" with length n,
for (int i = 0; i < arr.length; i++) {
    for (int j = i; j < arr.length; j++) {
        print(arr[i] + arr[j])
    }
}
```
Mathematically, for every `i`, `print(arr[i] + arr[j])` is running `n - i` times. So the formula will be:  
$(1 * n) + (1 * (n - 1)) + (1 * (n - 2)) + ...... + (1)$  
⇒ $1 + 2 + 3 + ....... + n$  
⇒ $n(n + 1) / 2$  
⇒ $n^2/2 + n/2$  
Using the rules of Analysis, the constant 2 will be removed and $n$ will be very small when complexity tends to infinity  
⇒ $n^2$

So the Time complexity is $O(n^2)$

## Analyzing Space complexity
- Never count the space used by the input and output unless interviewer asks
- Check for new variables which are allocating space
```java
// Given an integer array "arr" with length n
Array nums = int[]
int oneHundredth = n / 100

for (int i = 0; i < oneHundredth; i++) {
    nums.add(arr[i])
}
```
Space complexity = $O(n)$ as nums stores $n/100$ elements

## Introduction to recursion
- A problem solving method also known as a **Algorithmic Paradigm**
- Implemented using a function calling itself
- Computability Theory proves that any iterative algorithm(uses while and for loops) can be written recursively(use functions to simulate the same logic)
- Base case: conditions at the start of the recursive function that terminates the call  
e.g. Iterative
    ```java
    for (int i = 1; i <= 10; i++) {
        print(i)
    }
    ```
    Recursive
    ```java
    function fn(i):
        if i > 10:
            return

        print(i)
        fn(i + 1)
        return

    fn(1)
    ```
- The function calls "exists" until it returns. This means that whenver there is a function call to itself a new process will start running aditional version of the function. At the end base case will run, which will terminate the function and return call will start. As all the process are kept in a stack, the process is *First in Last out*. The last function will return first and then all the other after will return one by one
- Recursion shines when the we break down a problem into subproblem, whose solutions can be combined to solve original problem  
e.g. Fibonacci sequence: Sequence of numbers starting from 0, 1 and then each number is defined as the sum of previous two numbers.
Recurrence relation (An expression defining the next element of a sequence in terms of previous elements) for the same with initial values can be denoted by:  
$a_n = a_{n-1} + a_{n-2}, a{0} = a{1} = 1$  
This naturally leads us to recursion. Recurrence relation start at the base case and move towards higher values of $n$. **Recursion does the opposite**. It solves the problem by breaking it into smaller subsets of the larger problem until some base case is reached. From there, the total solution is reconstructed. Remember, recursion involves two conditions - 
    1. A base case where the problem is now simple enough to solve without further division
    2. A recursive case where the problem is written as a combination of simpler versions of itself
- **Procedure**
  - Take a concrete example of the given problem and split it into multiple sub problems to see where it leads
  - There will be a case beyond which you cannot split the problem anymore, this is the base case
  - The other subproblems will be your recursive cases
- Example of Fibonacci sequence
```java
function F(n)
  if n <= 1:    // Base case
    return n
  
  oneBack = F(n - 1)    // Recursive cases
  twoBack = F(n - 2)
  return oneBack + twoBack
```

## Solving the Second order linear recurrence relations
- There is a way to solve the Fibonacci number recurrence relation: $a_n = a_{n-1} + a_{n-2}, a{0} = a{1} = 1$
- This is a second order recurrence relation as the one element is dependent upon two previous elements in the sequence 
- The general form of the second order recurrence is  
$a_n = ra_{n - 1} + sa_{n - 2} + f(n)$  
If $f(n) = 0$, the recurrence is called homogeneous, else inhomongeneous   
For a second order relation of the form  
$a_n = ra_{n-1} + sa_{n-2} + f(n)$  
we can use the roots of the characteristic equation, we got this by replacing  
$a_n = x^2, a_{n - 1} = x^1, a{n - 2} = x^0 = 1$  
$x^2 - rx - s = 0$  
If we call the roots $x_0$ and $x_1$, then the homogeneous solution will be of the form  
$a_n^h = Ax_0^n + Bx_1^n$, if $x_0$ ≠ $x_1$  
or  
$a_n^h = Ax^n + Bnx^n$, if $x_0$ = $x_1 = x$ 
Solving the above equation for initial values can give us $A$ and $B$
- Solving the recurrence relation for Fibonacci sequence  
$a_n = a_{n - 1} + a_{n - 2}$  
The characteristic equation for the same is: $x^2 - x - 1 = 0$  
The roots are  
$x = \frac{ - b \pm \sqrt {b^2 - 4ac} }{2a} = \frac{ 1 + \sqrt {5} }{2}, \frac{ 1 - \sqrt {5} }{2}$  
The solution is of the form:  
$a_n = A(\frac{ 1 + \sqrt {5} }{2})^n + B(\frac{ 1 - \sqrt {5} }{2})^n$  
Using the initial value of $a_1 = 1$ and $a_0 = 0$, the equations are simplified to  
$A + B + \sqrt{5}(A - B) = 2$  
$A + B = 0$  
The values for $A$ and $B$ are $\frac{1}{\sqrt{5}}$ and $\frac{-1}{\sqrt{5}}$  
Plugging in these values in the original equation will give us  
$a_n = \frac{1}{\sqrt{5}}(\frac{ 1 + \sqrt {5} }{2})^n - \frac{1}{\sqrt{5}}(\frac{ 1 - \sqrt {5} }{2})^n$  
The value $\frac{ 1 + \sqrt {5} }{2}$ is the golden ratio which can be represented as:  
$\phi = \frac{ 1 + \sqrt {5} }{2}$ ≈ $1.618.....$  
We can say that $1 - \phi = \frac{ 1 - \sqrt {5} }{2}$ This rewrite the equation to:  
$a_n = \frac{1}{\sqrt{5}}(\phi^n - (1 - \phi)^n)$
We can use this equation to solve Fibonacci or Lucas sequence

## Arrays and Strings
- Technically Arrays cannot be resized but dynamic arrays can and strings are immutable
- Appeding to the list is [amortized $O(1)$](https://stackoverflow.com/questions/33044883/why-is-the-time-complexity-of-pythons-list-append-method-o1)
- The easy way to understand this is that once the size is decided for an array, let say 8 elements, then appending those elements will be $O(1)$, any other element after that will trigger reallocation for additional 8 elements, this reallocation will take time: $O(n)$, the distribution of these elements when amortized per element is $O(n) / n = O(1)$

## Arrays and Strings: Two Pointers
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