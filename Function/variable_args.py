from numpy import number


def multiplier(*numbers):
    out = 1
    for val in numbers:
        out *=val
    return out


  #ex call 


print(multiplier(2,4,5,6))
print(multiplier())
print(multiplier(3,3))      