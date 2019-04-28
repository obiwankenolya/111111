k = int(input())
m = int(input())
n = int(input())
a = n // k
if n % k != 0:
    a = n // k + 1
print(a * m * 2)
