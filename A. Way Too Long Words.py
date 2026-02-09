n = int(input())
for _ in range(n):
    word = input()
    size = len(word)
    if size > 10:
        num = str(size-2)
        
        print(word[0]+num+word[-1])
    else:
        print(word)
