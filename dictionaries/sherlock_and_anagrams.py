from collections import Counter


def sherlockAndAnagrams(string: str):
    count = 0
    for char_len in range(1, len(string) + 1):
        combinations_number = len(string) - char_len + 1
        combinations_list = []
        for index in range(combinations_number):
            combinations_list.append("".join(sorted(string[index: index + char_len])))
        countered_items = Counter(combinations_list)
        for item in countered_items:
            count += (countered_items[item] * (countered_items[item] - 1)) / 2
    return int(count)


result = sherlockAndAnagrams('cdcd')
assert result == 5

result = sherlockAndAnagrams('abcd')
assert result == 0
