#!/usr/bin/env python3

def print_fibonacci(n):
    a, b = 0, 1
    fibonacci_sequence = []

    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    print(fibonacci_sequence)

# Example: Printing the first 10 numbers of the Fibonacci sequence
print_fibonacci(10)
