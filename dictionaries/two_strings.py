def twoStrings(s1, s2):
    s1 = set(s1)
    s2 = set(s2)
    return "YES" if bool(s1.intersection(s2)) else "NO"

q = int(input())

for q_itr in range(q):
    s1 = input()
    s2 = input()
    result = twoStrings(s1, s2)
    print(result)