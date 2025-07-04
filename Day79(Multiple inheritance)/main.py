class name:
    def __init__(self , name):
        self.name = name;
        
    def show(self):
        print(f"name is {self.name}")
class role:
    def __init__(self , role):
        self.role= role
    def show(self):
        print(f"The role i {self.role}");
class Total(role , name):
    def __init__(self , name  , role):
        self.name = name ;
        self.role = role;
        print(f"name is {self.name} and the role is {self.role}");
a = Total("Parul" , "Girl")
print(a.name)
a.show();
print(Total.mro());
# mro :-method resolution order