# 1
def function_ex1(*args, **kwargs):
    sum = 0
    for i in args:
        if type(i) in [int, float]:
            sum += i
    return print(sum)


# function_ex1()


# 2
def function_ex2(index: int, totalSum: int, param_1: int, totalEvenSum: int, totalOddSum: int):
    myList = list(range(int(param_1) + 1))
    if index != param_1:
        if myList[index] % 2 == 0:
            totalEvenSum += myList[index]
        if myList[index] % 2 == 1:
            totalOddSum += myList[index]
        index += 1
        totalSum += myList[index]
        return function_ex2(index, totalSum, param_1, totalEvenSum, totalOddSum)
    else:
        if myList[index] % 2 == 0:
            totalEvenSum += myList[index]
        if myList[index] % 2 == 1:
            totalOddSum += myList[index]
        return totalSum, totalEvenSum, totalOddSum


"""sum, sumPar, sumImpar = function_ex2(index, totalSum, param_1, totalEvenSum, totalOddSum)
print("Suma totala: {}".format(str(sum)))
print("Suma numere pare: {}".format(str(sumPar)))
print("Suma numere impare: {}".format(str(sumImpar)))"""


# 3
def function_ex3():
    keyValue = input("Insert: ").lower().strip()
    if keyValue.isnumeric():
        return print(keyValue)
    else:
        return print(0)


# function_ex3()


param_1 = int(input("Input: "))
index = 0
totalSum = 0
totalOddSum = 0
totalEvenSum = 0


