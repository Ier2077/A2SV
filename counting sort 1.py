def countingSort(arr):
    # Write your code here
    count = [0]*100
    for elem in arr:
        count[elem] += 1
    return count
