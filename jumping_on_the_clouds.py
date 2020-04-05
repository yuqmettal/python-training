_ = int(input())
clouds = list(map(int, input().split()))

continue_next = False
jumps = 0

for ix, cloud in enumerate(clouds):
    if continue_next:
        continue_next = False
        continue
    if ix <= len(clouds) - 3 and clouds[ix + 2] == 0:
        continue_next = True
    if ix != len(clouds) - 1:
        jumps += 1

print(jumps)