_, q = [int(x) for x in input().split()]
array = input().split()

result = {"0": "EVEN", "1": "ODD"}

for _ in range(q):
    query = [int(x) for x in input().split()]
    if query[0] == 0:
        print(result[array[query[-1] - 1]])
        continue
    _, index = query
    array[index - 1] = "1" if array[index - 1] == "0" else "0"