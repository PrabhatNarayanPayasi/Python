# instance variable har object ke sath  associated hote hai
# matlb ki har object ka apna ek instance variable hota hai
# instance variable ko self keyword ke through
# access kiya ja skta hai 

'''
Instance Variable ka Importance:
Object-specific data ko store karna. Jaise ki ek car ki brand ya color, ya ek student ka name ya marks.
Har object ka apna unique data hota hai, aur instance variable uss object ko apni state ya characteristics dene ka kaam karta hai.
'''
# class person:
#     def __init__(self , name , age):
#         self.name = name; # ye hai instanse variable 
#         self.age = age; # ye hai instance variable
#     def show(self):
#         print(f"name is {self.name} and age is {self.age}");
# a = person("Prabhat" , 19);
# a.show()



# class variable ek specific class se associated hote hai sare object jo use class se bane hai unke liye 
# ek hi value hoti hai us variable ki 
# ye variable class level per define hote hai aur self nhi direct class name ya 
# instance ke through access kiye jate hai

'''

Class Variable ka Importance:
Shared data ko store karna jo sab objects ke liye common ho. Jaise ki sab cars ke liye ek hi number of wheels hote hain, ya sab students ka same school name hota hai.
Agar aapko kisi specific class ke sare objects ke liye ek common value rakhni ho, to class variables ka use kiya jata hai.
'''
class Hero:
    # name = "Hero"
    name = 3;
    def __init__(self, naam, age):
        self.naam = naam;
        self.age = age;
    def details(self):
        print(f"naam is {self.naam} and age is {self.age}");
b = Hero("narayan" , 34)
# b.name() isko directly access karo method ko call nhi karna 
print(b.name)
b.details()

# Yeh concepts aapko code ko structure dene, memory manage karne, aur object-specific aur class-specific data ko differentiate karne mein madad karte hain.