def add(a,b,c,d):
    return a+b+c+d



if __name__ ==    "__main__":
    #print(add(a=10,b=3,c=3,d=3))
    out = add(20,20)
    print(out)
    out = add(20,20,10)
    print(out)
    out = add(20,20,10,20)
    print(out)
    out = add(20,20,c=10)
    print(out)
    out = add(20,20,d=20)
    print(out)
    out = add(20,20,d=20,c=10)
    print(out)