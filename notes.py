import uuid
notes=[]

def add():
    text=input("\nEnter a Note  ")
    id1=str(uuid.uuid4())
    note={"id":id1,"text":text}
    notes.append(note)
    print(f"({note['text']})  Append Sucsess")
def linote():
    if not notes:
        print("Not Found,Note is Empty")
        return
    for i in notes:
        print(f"ID : {i['id']}, Note : {i['text'][:10]}")
def retnote():
    if not notes:
        print("Not Found,Note is Empty")
        return
    id0=input("\nEnter a ID Notes   ")
    for i in notes:
            if i['id']==id0:
                print(f"ID : {i['id']}, Note : {i['text']}")
                return
    print("Error  ID, Enter Valid ID")
def delnote():
    id0=input("\nEnter a ID Note    ")
    for i in notes:
        if i['id']==id0:
            notes.remove(i)
            return
    print("Error  ID, Enter Valid ID")
def serchnote():
    key=input("\nEnter a Keyword for Serch  ")
    serch=[note for note in notes if key.lower() in note['text'].lower()]
    if not serch:
        print("Not Found")
        return
    for i in serch:
        print(f" ID : {i['id']}, Note : {i['text']} ")




while True:
    print("\n1.Note Adding")
    print("2.Note Listing")
    print("3.Note Retrieval")
    print("4.Note Deletion")
    print("5.Note Serch")
    print("6.Exit")
    a=input("\nEnter a Variant   ")

    if a=="1":
        add()
    elif a=="2":
        linote()
    elif a=="3":
        retnote()
    elif a=="4":
        delnote()
    elif a=="5":
        serchnote()
    elif a=="6":
        print("Exit Program")
        break
    else:
        print("Invalid Variant")
