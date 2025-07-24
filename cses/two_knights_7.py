n = int(input())

for k in range(1, n + 1):
    size = k**2

    total = size * (size - 1) // 2

    bad = 0
    bad += 8 * ((k - 4) ** 2)
    bad += 6 * (k - 4) * 4
    bad += 4 * (k - 3) * 4
    bad += 3 * 8
    bad += 2 * 4
    bad //= 2

    print(total - bad)
