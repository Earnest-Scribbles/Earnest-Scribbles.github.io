---
title: Introduction to big O
pubDate: 2025-11-02
chapter: 1
draft: false
notebookTitle: Amazon Cloud Attack and Defense Bootcamp
---
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