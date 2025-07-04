#  ye ek tarreka hai child class ke ander parent class
#  ke methods ko change karne ka 
# class Animal:
#     def Sound(self):
#         print("Animal Sound");
# class Dog:
#     def dog(self):
#         print("Dog sound");
# animal = Animal();
# dog = Dog();
# animal.Sound();
# dog.dog();

#  maaatlb method overriding ye hota hai ki jab parent class ke kisi method ka veraion child class define karta hai . 
#  iska matlb hai ki subclass apne parent class ke method ko override karta hai 
# apne specific behaiviour ke liye . 
# matlb method overriding tab karte hai jab hame parent class ke behaiviour ko change karna ho . 

class car:
    def __init__(self , name , price):
        self.name = name;
        self.price = price;
    def show(self):
        print(f"name of the car is {self.name} and price is {self.price}");
class Bcar(car):
    def __init__(self , name , price , brand):
        self.brand = brand;
        super().__init__( name  , price)
    def show(self):
        print(f"car is {self.name} price is {self.price} and brand is {self.brand}");
c = car("Bugati" , "2Cr");
B = Bcar("lamborginni" ," 8Cr " , "Branded");

B.show();
c.show();



'''
 
Same method name in parent and child class.
Child class method implementation is different from parent class.
Child class method is executed instead of parent class method when you call the method on an instance of the child class.
 
 
 
 
 
Agar child class mein ek method hai 
jo parent class ke method
ko replace karta hai (with a new implementation), aur aap 
child class ka method call karte ho, toh hum keh sakte hain ki method overriding ho rahi hai.'''