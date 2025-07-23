n = int(input())

nums = list(map(int, input().strip().split()))
ans = 0
for i in range(1, len(nums)):
    if nums[i] < nums[i - 1]:
        ans += nums[i - 1] - nums[i]
        nums[i] = nums[i - 1]

print(ans)
