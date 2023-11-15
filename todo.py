def add(tolist):
    t_id=len(tolist)+1
    des=input("Enter description ")
    if not des:
        print("Error des")
        return
    pro=input("Enter prority(high,medium, low) ").lower()
    if pro not in ["high","medium", "low"]:
        print(" Error prority:Prority defaoult low \n")
        pro="low"
    tolist.append({"id":t_id,"des":des,"pro":pro,"comp":False})
    print(f"\n{t_id} added")
def remo(tolist):
    t_id=int(input("Enter a remove Id "))
    for re in tolist:
        if re["id"]==t_id:
            tolist.remove(re)
            print(f"{t_id} removed")
            return
    print("Error: not found")
def list_tasks(tolist):
    if  not tolist:
        print("Error:not found ")
    else:
        for task in tolist:
            print(f"Task ID {task['id']}, Task Description: {task['des']},   pro : {task['pro']}, Task comp: {task['comp']}")
def comp(tolist):
    marked = int(input("Enter id for marked complete"))
    for task in tolist:
        if task['id'] == marked:
            task['comp'] = True
            return
    print("No such ID")

def priority(tolist):
    if not tolist:
        print("No tasks in the to-do list.")
        return
    priority = {"low": 1, "medium": 2, "high": 3}
    sor = sorted(tolist, key=lambda x: priority[x["pro"]])
    for task in sor:
        print(f"ID: {task['id']}, Des: {task['des']}, Pro: {task['pro']},task comp: {task['comp']}")

tolist=[]
while True:
        print("\n\n1.Add")
        print("2.Remove")
        print("3.List")
        print("4.Completed")
        print("5.priority")
        print("6.Exit")




        a=input("Enter a Variant")
        if a=="1":
            add(tolist)
        elif a=="2":
            remo(tolist)
        elif a=="3":
            list_tasks(tolist)
        elif a=="4":
            comp(tolist)
        elif a=="5":
            priority(tolist)
        elif a=="6":
            print("Exit program")
            break
        else:
            print("\n\n Error: Enter a true Variant ")
