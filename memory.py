size=5
memory=[]
page=[]
def allocate(data):
    if len(memory)<size:
        index=len(memory)
        page1={"data":data,"index":index}
        page.append(index)
        memory.append(page1)
    else:
        old=page.pop(0)
        page1={"data":data,"index":old}
        page.append(old)
def access(index):
    if 0<=index<len(memory):
         print(f" Data : {memory[index]['data']}, Index :: {memory[index]['index']}")
    else:
        print("Invalid Index")
def disp():
    for count,page in enumerate(memory,start=0):
        print(f"Data:{page['data']}, Index : {page['index']}")
    if len(memory)==size:
            print("Full")
    else:
        print("Memory is empty")

while True:
        print("\n1. Allocate Memory")
        print("2. Access Memory")
        print("3. Display current status")
        print("4. Exit")

        a = input("\nEnter a Variant    ")
        if a == "1":
            data = input("\nEnter data  ")
            allocate(data)
        elif a == "2":
            index = int(input("\nEnter index    "))
            access(index)
        elif a == "3":
            disp()
        elif a=="4":
            print("Exit Program")
            break
        else:
            print("Invalid Variant")

