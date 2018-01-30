# Lab 2: Introduction to Recursion

This lab introduces you to recursion by implementing recursive solutions to two commonly defined recursive functions:

* n! -- n factorial is often defined recursively: n! = n * (n - 1)!
* Finding the nth Fibonacci number, where the Fibonacci sequence is defined recursively as Fib(n) = 1 for n = 1, 2 and as Fib(n - 1) + Fib(n - 2) for n > 2

In the `csc131.lab02` module, you will find stubs for these operations, as well as a stub for computing n factorial using iteration (as opposed to recursion). Your goal is to make all the unit tests defined in `test_suite.py` to pass. It is recommended that you commit after implementing each of the TODO statements in this module.

If you wish to see the values of these functions in advance of your coding efforts, visit [https://www.wolframalpha.com/](https://www.wolframalpha.com/) where you compute various values of n! or fib(n).