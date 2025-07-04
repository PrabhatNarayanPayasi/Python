#  kabhi kabhi hame child class se parent class ke method ko call karna padta hai
# to iske liye ham super keyword ka use karte hai . 
class Parent:
    def parent_methhod(self):
        print("I am a prarent method");
class Child(Parent):
    def parent_methhod(self):
        print("Under child")
    def child_method(self):
        print("I am a child method");
        super().parent_methhod()
a = Child();
a.child_method();
a.parent_methhod();



#  Super with constructor 
# isme jo parent class ke cheeje hia unhe cchild me bina 
# dobara likhe hi direct acces kar skte hai super keyword ka use karke .

class Emp:
    def __init__(self , name , id):
        self.name = name;
        self.id = id;
class Prog(Emp):
    def __init__(self , name  , id , role):
        self.role = role;
        super().__init__(name , id);
prabhat = Emp("Prabhat" , 111);
shiva = Prog("shiva" , 124 , "Devloper");
print(prabhat.id);
         