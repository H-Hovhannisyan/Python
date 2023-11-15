def val_user(fun):

        def wrap1(*args):
            if  len(args[0])>=5 and len(args[0])<=20 and args[0].isalnum() and\
                args[0].lower() not in {"admin","root","user"}:
                return fun(*args)
            else:
                raise ValueError("Invalid Name! Enter Again(6-19 Character and can't this name(admin,root,user))")


        return wrap1
def val_mail(fun1):
    def wrap2(*args):
        if "@" in args[1][1:] and "." in args[1][-4:]:
            return fun1(*args)
        else:
            raise ValueError("Invalid Mail")
    return wrap2

def val_phone(fun2):
    def wrap2(*args):
        if (args[2][0] == "0" and len(args[2])==9 and args[2].isdigit()) or (args[2][0:4]=="+374" and len(args[2])==12 and args[2][5:].isdigit()):
            return(fun2(*args))
        else:
            raise ValueError("Invalid phone")
    return wrap2
def val_password(fun3):
    def wrap3(*args):
        flag1=False
        flag2=False
        flag3=False
        if (len(args[3])>=8):
            for i in args[3]:
                if ("a"<=i<="z"):
                    flag1=True
                if("A"<=i<="Z"):
                    flag2=True
                if ("0"<=i<="9"):
                    flag3=True
                if flag1 and flag2 and flag3:
                    return fun3(*args)

            raise ValueError("Invalid Password")
        else:
            raise ValueError("Invalid Password")

    return wrap3
def rep_password(fun4):
    def wrap4(*args):
        if args[3]==args[4]:

            return fun4(*args)
        else:
            raise ValueError("Repeat Password Error")

    return wrap4

@rep_password
@val_password
@val_phone
@val_mail
@val_user
def username1(username,email,phone,password,rep_password):
    return (username,email,phone,password,rep_password)
while True:
        a=input("Enter '/' to Exit: Enter to Continue")
        if a=="/":
            break
        username = input("Enter Username")
        mail = input("Enter Mail ")
        phone = input("Enter Phone-Number ...")
        password = input("Enter password ")
        rep_password = input("Repeat password ")
        try:
            username1(username,mail,phone,password,rep_password)
            print("Success")
            break
        except ValueError as e:
            print(e)
