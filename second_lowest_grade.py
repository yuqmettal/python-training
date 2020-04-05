list_ = [
    ['Harry', 37.21],
    ['Berry', 37.21],
    ['Tina', 37.2],
    ['Akriti', 41],
    ['Harsh', 39],
    ]
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     list_.append([name, score])

second_lowest_grade = sorted(list(set([x[1] for x in list_])))[1]
students = [x[0] for x in list_ if x[1] == second_lowest_grade]
print(*sorted(students), sep="\n")