a = int(input())
b = int(input())
c = int(input())

if a==0:
    print(-c/b)
else:
    d = b**2 - 4 * a * c
    x1 = (-b - d ** 0.5)/(2 * a)
    x2 = (-b + d ** 0.5) / (2 * a)
    print(x1, x2)
