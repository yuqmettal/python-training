input_string = input().strip()
string_length = int(input())

string_repeated = (string_length // len(input_string))
total_times = string_repeated * input_string.count('a')
remain_string_chars = string_length - (string_repeated * len(input_string))
if remain_string_chars != 0:
    total_times += input_string[:remain_string_chars].count('a')

print(total_times)