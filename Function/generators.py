#generators are special func in python
#that can be used to generate a sequence of values instead of 
# returning the value from the func once we put the value in to memory space
#using yield keyword and then we can the next (func) to get the next value generators are fast compared to lists

from re import A


def cube(limit):
    for  i in range(1,limit+1):
        yield i**3

def fib(limit):
    a,b = 0,1
    for i in range(limit):
      yield a
    a,b = b,a+b        

#ex call


for c in cube (10):
    print(c)

for f in fib(15):
    print(f,end='|')    



#wap to generate a list of even sqr using generators 
# wap to generate a list of acronyms from a list of word using generatros & *args


# def even(limit):

#     for i in range(1,limit+1):
#         if i%2==0
#         #yield i/2
#         yield i*2


# for e in even (2):
#     print(e)        

