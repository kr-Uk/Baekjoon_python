divisor, multiple = 1, 1

a, b = map(int, input().split())

n = 2

while n <= max(a, b):
    if a % n == 0 and b % n == 0:
        divisor *= n
        a = a // n
        b = b // n
        n = 2
    else:
        n += 1

print(divisor)
multiple = divisor * a * b
print(multiple)
