movements_nuber = int(input())
movement_directions = list(input())

sea_level = 0
valleys = 0

for ix, movement in enumerate(movement_directions):
    sea_level = sea_level + 1 if movement == 'U' else sea_level - 1
    if sea_level == 0 and ix > 0 and movement == 'U':
        valleys += 1

print(valleys)