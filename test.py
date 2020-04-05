import math
import os
import random
import re
import sys

def arrayManipulation(n: int, queries: list):
    array = [0] * n
    for query in queries:
        first, last, value = query
        for column in range(first -1, last):
            array[column] += value
    return max(array)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()