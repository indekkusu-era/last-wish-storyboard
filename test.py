def factor(num: int):
    counter = 1
    a = 10 ** (len(str(num)) - 1)
    for i, n in enumerate(str(num)):
        print(a // counter, n)
        counter *= 10

factor(1324)
