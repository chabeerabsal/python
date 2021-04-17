#generator functions
#sequence of values
def test():
    yield  'a'
    yield  'b'
    yield 'c'
    yield 'd'
result=test()
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(type(result))