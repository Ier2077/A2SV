n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

i = j = 0
output = []

while i < n and j < m:
    if a[i] <= b[j]:
        output.append(a[i])
        i += 1
    else:
        output.append(b[j])
        j += 1


output.extend(a[i:])
output.extend(b[j:])

print(*output)