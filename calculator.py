def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    try:
        return a/b
    except ZeroDivisionError as e:
        print("\n",e,"\n")
        return None

while True:
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Exit")


        d=input("\n Enter a operation \t")
        if d=="5":
            print("\n Exit ")
            break
        if d not in ["1","2","3","4"]:
            print("\n Invalid input \n")
            continue
        try:
            a=float(input("\n Enter Frist Number \t"))
            b=float(input("\n Enter a Second Number \t"))
        except ValueError as e:
            print("\nError Enter Valid Number\n",e)
            print("\n")
            continue
        if d=="1":
            res=add(a,b)
            print(f"\n {a} + {b} = {res} \n")
        elif d=="2":
            res=sub(a,b)
            print(f"\n {a} - {b} = {res} \n")
        elif d=="3":
            res=mul(a,b)
            print(f"\n {a} * {b} = {res} \n")
        elif d=="4":
            res=div(a,b)
            if res is not None:
                print(f"\n {a} / {b} = {res} \n")

