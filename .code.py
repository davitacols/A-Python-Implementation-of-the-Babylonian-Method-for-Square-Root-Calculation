import math

def my_sqrt(a):
    x = a/2.0
    y = (x + a/x) / 2.0
    while abs(y-x) > 0.0000000001:
        x = y
        y = (x + a/x) / 2.0
    return y

def test_sqrt():
    print("a = {} | my_sqrt(a) = {:.11f} | math.sqrt(a) = {} | diff = {:.11f}")
    print("------------------------------------------------------------")
    for a in range(1, 26):
        my_sqrt_val = my_sqrt(a)
        math_sqrt_val = math.sqrt(a)
        diff = abs(my_sqrt_val - math_sqrt_val)
        print("a = {} | my_sqrt(a) = {:.11f} | math.sqrt(a) = {} | diff = {:.11f}"
              .format(a, my_sqrt_val, math_sqrt_val, diff))
        
test_sqrt()
