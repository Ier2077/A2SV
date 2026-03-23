length, limit = map(int, input().split())
nums = list(map(int, input().split()))

current_sum = 0
best = 0
start = 0

for end in range(length):
    current_sum += nums[end]

    while current_sum > limit:
        current_sum -= nums[start]
        start += 1

    best = max(best, end - start + 1)

print(best)
