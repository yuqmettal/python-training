def minimumBribes(queue: list):
    movements = 0
    for ix, val in enumerate(queue):
        if val - 3 > ix:
            print("Too chaotic")
            return

        for pos in range(max(0, val - 2), ix):
            if queue[pos] > queue[ix]:
                movements += 1
    print(movements)


test_numbers = int(input())
for _ in range(test_numbers):
    _ = int(input())
    queue = list(map(int, input().split()))
    minimumBribes(queue)
