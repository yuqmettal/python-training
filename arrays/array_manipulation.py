n, inputs = [int(n) for n in input().split(" ")]
list_ = [0]*(n+1)
for _ in range(inputs):
    x, y, incr = [int(n) for n in input().split(" ")]
    list_[x-1] += incr
    if y <= len(list_):
        list_[y] -= incr

max_ = 0
accumulator = 0
for i in list_:
    accumulator += i
    if max_ < accumulator: max_ = accumulator

print(max_)