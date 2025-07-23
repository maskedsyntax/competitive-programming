n = int(input())

nums = list(map(int, input().strip().split()))

sum_ = n*(n+1)//2
print(sum_ - sum(nums))
