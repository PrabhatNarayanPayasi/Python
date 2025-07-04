class Emp:
    def __init__(self , name  , id):
        self.name= name
        self.id = id
    def show(self):
        print(f"The name of emp {self.name} is {self.id}")


class Programmer(Emp):
    def showl(self):
        print("Defaulte langiage is python")
a = Emp("Rohandas" , 420)
a1 = Programmer("Shiva" , 142)
a.show();
a1.showl();

class Code(Programmer):
    def showD(self):
        print("Class name is Coder")
a2 = Code("narayan"  , 124);
a2.show();
a2.showD();


class A(Programmer,Code):
    def detail():
        print("This is Multiple inheritance")
b = A("Payasi" , 124);
b.showl();