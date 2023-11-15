def counter(value=0):
    count=value
    def inc(amount=1):
        nonlocal count;
        count+=amount
    def dec(amount=1):
        nonlocal count;
        count-=amount
    def get_res():
        return count
    return inc,dec,get_res


inc,dec,get_res=counter()
inc()
dec()
inc(5)
dec(2)
print(get_res())
inc1,dec1,get_res1=counter()
inc1(2)
dec1(2)
inc1()
print(get_res1())
