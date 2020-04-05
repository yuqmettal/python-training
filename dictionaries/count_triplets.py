from collections import Counter

def countTriplets(numbers_array: list, r: int):
    first_dict = Counter()
    second_dict = Counter()
    counter = 0
    for item in numbers_array:
        if item in second_dict:
            counter += second_dict[item]
        if item in first_dict:
            second_dict[item * r] += first_dict[item]
        first_dict[item * r] += 1
    return counter

result = countTriplets([1, 5, 5, 25, 125], 5)
assert result == 4