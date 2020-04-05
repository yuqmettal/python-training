def minimumSwaps(arr: list) -> int:
    swaps = 0
    temp = [0] * (len(arr) + 1)
    for ix in range(len(arr)):
        temp[arr[ix]] = ix
    print(temp)
    for ix in range(len(arr)):
        if arr[ix] != ix + 1:
            swaps +=1
            index = temp[ix + 1]
            current_value = arr[ix]
            arr[ix], arr[index] = ix + 1, arr[ix]
            temp[ix + 1], temp[current_value] = ix, temp[ix + 1]
    return swaps
            

# n = int(input())
# arr = list(map(int, input().rstrip().split()))
arr = [1, 3, 5, 2, 4, 6, 7]
res = minimumSwaps(arr)
print(res)