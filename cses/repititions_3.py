s = input()

cnt = 1
max_ = 1

for i in range(1,len(s)):
    if s[i] == s[i-1]:
        cnt += 1
        max_ = max(max_, cnt)
    else:
        cnt = 1

print(max_)
