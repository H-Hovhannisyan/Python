def val_user(fun):

        def wrap1(name):
            if  len(name)>=5 and len(name)<=20 and name.isalnum() and\
                name.lower() not in {"admin","root","user"}:
                return fun(name)
            else:
                print("Invalid Name! Enter Again(6-19 Character and can't this name(admin,root,user))")
                return

        return wrap1
def val_mail(fun1):
    def wrap2(mail):
        if "@" in mail[1:] and "." in mail[-4:]:
            return fun1(mail)
        else:
            print("Invalid Mail")
            return
    return wrap2

def val_phone(fun2):
    def wrap2(phone):
        if (phone[0] == "0" and len(phone)==9 and phone.isdigit()) or (phone[0:4]=="+374" and len(phone)==12 and phone[5:].isdigit()):
            return(fun2(phone))
        else:
            print("Invalid phone")
            return
    return wrap2
def val_password(fun3):
    def wrap3(password):
        flag1=False
        flag2=False
        flag3=False
        if (len(password)>=8):
            for i in password:
                if ("a"<=i<="z"):
                    flag1=True
                if("A"<=i<="Z"):
                    flag2=True
                if ("0"<=i<="9"):
                    flag3=True
                if flag1 and flag2 and flag3:
                    return fun3(password)

            print("Invalid Password")
        else:
            print("Invalid Password")
            return
    return wrap3
def rep_password(fun4):
    def wrap4(password,rep_password):
        if rep_password==password:

            return fun4(password,rep_password)
        else:
            print("Repeat Password Error")
            return
    return wrap4

@val_user
def username1(username):
    return username
@val_mail
def mail1(mail):
    return mail
@val_phone
def phone1(phone):
    return phone
@val_password
def password1(password):
    return password
@rep_password
def rep_password1(password,repeat_password):
    return password == repeat_password
while True:
        a=input("Enter '/' to Exit: Enter to Continue")
        if a=="/":
            break
        username = input("Enter Username")
        if(username1(username)):
            mail = input("Enter Mail ")
            if(mail1(mail)):
                phone = input("Enter Phone-Number ...")
                if(phone1(phone)):
                    password = input("Enter password ")
                    if(password1(password)):
                        rep_password = input("Repeat password ")
                        if(rep_password1(password, rep_password)):
                            print("You Registered")
                        else:
                            break
                    else:
                        break
                else:
                    break
            else:
                break
        else:
            break
