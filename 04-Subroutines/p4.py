def f(number,even):
    a=str(number)
    c=0
    d=0
    for i in a:
        b=int(i)
        if b%2==0:
            c=c+b
        if b%2!=0:
            d=d+b
    if even==True:
        return c
    if even==False:
        return d

