'''

lamda function bhi expression ki tareh hote hai.
hame lambda funtion ka use tab karna hai  jab ham chahte hai ki hama code one liner ho jaye matlb ek line me ho jaye.
lambda function ka use ham tab karte hai jab hame kabhi kabhi ek function ko as a argument doosre function ke andar pass karna hota hai.
ye anonyms function hote hai matlb inka naam nahi hota hai . 

'''
# normal function ese hota hai : -
# def name():
#     print("hello")
# name() 
# lekin agar m ise hi lambda function ke roop me likhu to :-
print(lambda name:print("Hello Lambda"))
# YE CODE EK FUNCTION PRINT KAREGA KYOKI LAMBDA FUNCTION EK function return karta hai . 
# agar ham lambda function ka output print karvana chahte hai to hame function ko call karna padega jaise neeche kiye hai .
(lambda name: print("Hello Lambda"))("John")
(lambda name:print(f"hello {name}"));
(input("Enter name"))

# aur achhe se samajhte hai . 
naaam = lambda naam:print(naam)
print(naaam("Shiva"))



'''

Lambda function zyada short aur quick tasks ke liye hai, jab aapko ek simple function likhna ho. 
Jab aapko complex logic chahiye,
ya function ko reuse karna ho, to def function better hota hai.
Lambda ka main faida hai ki aap ek line me quick function bana sakte hain,
lekin def functions zyada readable aur flexible hote hain.

'''

add = lambda x,y:x+y;
print(add(3,4))
print((lambda x,y :x*y) (4,5))

#yaha pe hamne lambda function banaya aur uske just bagal me hi function ko call kar diya .
#ye inline ananomous hote hai . 
