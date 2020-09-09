import math_lib as ml

def calc(a,b):
    add = ml.add(a,b)
    div = ml.div(a,b)
    print("a+b = ", add)
    print("a/b = ", div)
    return

if __name__ =='__main__':
    calc(8,4)