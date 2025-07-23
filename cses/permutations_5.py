# from typing import list

n = int(input())


def get_odds(n: int) -> list:
    odds = []
    for i in range(1, n + 1, 2):
        if i % 2 != 0:
            odds.append(i)

    return odds


def get_evens(n: int) -> list:
    evens = []
    for i in range(2, n + 1, 2):
        if i % 2 == 0:
            evens.append(i)

    return evens


def solve(n: int) -> list:
    if n == 3 or n == 2:
        return []

    return get_evens(n) + get_odds(n)


ans = solve(n)
if len(ans) == 0:
    print("NO SOLUTION")
else:
    for i in ans:
        print(i, end=" ")

    print()
