def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum
    
#print(add(3,35,7,3,5,2))

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)