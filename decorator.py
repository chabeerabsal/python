def decorate_division(func):
    def inner(no1,no2):
        if no2==0:
            print('check no2 value')
            return
        else:
            return func(no1,no2)
    return inner
@decorate_division
def division(no1,no2):
    return no1/no2

print(division(100,0))
#extending functionality of an existing function,without modifying  it.