#1
initialList = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(initialList)
#2
ascInitialList = sorted(initialList, reverse=False)
print(ascInitialList)
#3
descInitialList = sorted(initialList, reverse=True)
print(descInitialList)
#4
evenNumbersList = sorted(initialList, reverse=False)[::2]
print(evenNumbersList)
#5
oddNumbersList = sorted(initialList, reverse=False)[1::2]
print(oddNumbersList)
#6
threeMultiples = sorted(initialList, reverse=False)[2::3]
print(threeMultiples)