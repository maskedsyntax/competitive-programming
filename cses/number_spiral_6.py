t = int(input())


def solve(r: int, c: int) -> None:
    value = 0
    if r == c:
        value = r**2 - r + 1
    elif r > c:
        if r % 2 == 0:
            value = r**2 - c + 1
        else:
            value = (r - 1) ** 2 + c
    else:
        if c % 2 == 0:
            value = (c - 1) ** 2 + r
        else:
            value = c**2 - r + 1

    print(value)


for i in range(t):
    y, x = input().strip().split()

    solve(int(y), int(x))


"""

for (r,c)
if r == c:
    value = r**2 - r + 1
elif r > c:
    if r is even:
        value = r**2 - c + 1
    else:
        value = (r-1)**2 + c
else:
    if c is even:
        value = (c-1)**2 + r
    else:
        value = c**2 - r + 1

"""
