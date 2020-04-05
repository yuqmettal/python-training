_, rotations = list(map(int, input().split()))
collection = input().split()

left_movements = rotations if rotations <= len(collection) else rotations - ((rotations // len(collection)) * len(collection))
print(*collection[left_movements:], end=' ')
print(*collection[:left_movements])