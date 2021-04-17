def  firstNnumbers(num):
    n=1
    while n<=num:
        yield  n
        n=n+1
values=firstNnumbers(10)
for i in values:
    print(i)
print(values)
print(type(values))
