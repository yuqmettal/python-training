def fizzbuzz(n):
    for i in range(1, n + 1):
        result = ""
        if i % 3 == 0:
            result += "Fizz"
        if i % 5 == 0:
            result += "Buzz"
        if len(result) > 0:
            print(result)
            continue
        print(i)

fizzbuzz(15)