

class employee:
    def __init__(self):
        self.uid=input("Enter ID");
        self.name=input("Enter name");
        self.age=input("Enter age");
        self.salary=input("Enter salary"); 
        self.designation=input("Enter designation");

    def display(self):
        print("ID: ",self.uid)
        print("name: ",self.name)
        print("age: ",self.age)
        print("salary: ",self.salary)
        print("designation: ",self.designation)
   

        

e=employee()
e.display()