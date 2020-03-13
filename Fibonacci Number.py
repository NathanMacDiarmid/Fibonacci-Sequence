
def fib(n):
    lst = []
    for i in range(n + 1):
        if i == 0:
            lst.append(0)
        elif i == 1:
            lst.append(1)
        elif i > 1:
            x = lst[-1] + lst[-2]
            lst.append(x)
    return lst

print(fib(int(input("Please enter a number:"))))