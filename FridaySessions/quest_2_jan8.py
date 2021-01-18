# Write a function to compute the value of n in the Fibonacci Sequence
# Examples:
# f(7) returns 13
# f(1) returns 1


def f(n):
    a = 0
    b = 1
    x = 0
    if n == 0:
        return print(a)
    while x < n - 1:
        c = b
        b += a
        a = c
        x += 1
    print(b)

n = int(input("Input the nth position in Fibonacci Sequence: "))
f(n)