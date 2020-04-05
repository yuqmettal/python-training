# _ = input()
# a = [int(x) for x in input().split()]
# b = [int(x) for x in input().split()]

a = [1, 2, 3, 4, 5]
b = [4, 5, 3, 2, 10]

print(*[sum(x) for x in zip(a, b)])
