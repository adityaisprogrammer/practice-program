class employee:
     def __init__(self, name, salary, role):
         self.name = name 
         self.salary = salary
         self.role = role

aditya = employee("aditya", 1000000, "Senior programmer")
harry = employee("harry", 100000, "junior programmer")

input_1 = input("Which employee information do you want (harry/aditya) :")

if input_1.lower()=='aditya':
    input_1 = input("what information do you want of aditya:")
    if input_1.lower()=="name":
        print("the employee name is",aditya.name)
    elif input_1.lower()=="salary":
        print("the employee salary is",aditya.salary)
    elif input_1.lower()=="role":
        print("the employee role is",aditya.role)
    else:
        print("No other action to take")    
elif input_1.lower()=='harry':
    input_1 = input("what information do you want of harry:")
    if input_1.lower()=="name":
        print("the employee name is",harry.name)
    elif input_1.lower()=="salary":
        print("the employee salary is",harry.salary)
    elif input_1.lower()=="role":
        print("the employee role is",harry.role)
    else:
        print("No other action to take")            
else:
    print("this is not a employee name")
