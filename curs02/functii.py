def functie_1(param_1, param_2, *args, **kwargs):
    print(type(args))
    print(type(kwargs))
    sum = param_1+param_2
    for i in args:
        sum += i
    for i in kwargs.values():
        sum += i
    return sum


print(functie_1(1, 5, 4, 5, v=3, c=6))
