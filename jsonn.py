
path="file.json"
def load():
    data=[]
    try:
        with open(path,"r") as f:
            line=f.readlines()
            for i in line:
                data.append(eval(i))
    except FileNotFoundError as e:
        print(e)
    return data
def save(data):
    with open(path,"w") as f:
        for i in data:
            f.write(str(i)+"\n")
def add():
    data=load()
    text={}
    for key in input("Enter key  ").split(','):
        value = input("Enter value  ")
        text[key.strip()] = value.strip()
    data.append(text)
    save(data)
    print("Data Added.")
def retdata():
    data=load()
    if not data:
        print("Not Found")
    else:
        for i in data:
            print(i)
def update():
    data=load()
    if not data:
        print("Not Found")
        return
    key=input("Enter Key    ")
    value=input("Enter a New Value  ")
    flag=False
    for i in data:
        if key in i:
            flag=True
            i[key]=value
    if flag:
        save(data)
        print("Data Update Success")
    else:
        print("Not Found")
def deldata():
    data=load()
    if not data:
        print("Not Found")
        return
    key=input("Enter a Key to Delete    ")
    data1=[x for x in data if key not in x]
    if len(data1) < len(data):
        save(data1)
        print("Data Success Deleted")
    else:
        print("Error")




while True:
    print("\n1.Data Storage")
    print("2.Data Retrieval")
    print("3.Data Update")
    print("4.Data Delete")
    print("5.Exit")
    a=input("\nEnter a Variant  ")

    if a=="1":
        add()
    elif a=="2":
        retdata()
    elif a=="3":
        update()
    elif a=="4":
        deldata()
    elif a=="5":
        print("Exit Program")
        break
    else:
        print("Invalid  Variant")
