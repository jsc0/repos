def first():
    print("First Function")

def second():
    print("Second function")

def third():
    print("Third function")

def default():
    print("Default function")


var : int = 2

funcs : dict = {0: first,
        1: second,
        2: third}

final = funcs.get(var, default)

final()