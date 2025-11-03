---
title: "Recursion"
pubDate: 2024-11-16
chapter: 2
draft: false
notebookTitle: "Leetcode - Interview Crash Course"
---
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