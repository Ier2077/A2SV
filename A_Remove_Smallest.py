t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    sorted_arr = sorted(set(arr))

    if len(sorted_arr) <= 1:
        print("YES")
        continue

    for i in range(len(sorted_arr) - 1):
        if sorted_arr[i + 1] - sorted_arr[i] != 1:
            print("NO")
            break
    else:
        print("YES")