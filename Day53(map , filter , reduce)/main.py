'''
  
  jaise m agar ek function bnata hu jo cube karta hain item ka 
  to vo simple ans de dega agar m list par vahi cheej karna chahta hu to mujhe bahut sra code likhna padega 
  
'''
def cube(x):
    return x*x*x;
print(cube(2)) # ab agar me yahi cheej list pe apply karna chahu to

l = [1,2,3,4,5,6,7,8,8,10,11,12];
# newl = [];
# for i in l:
#   newl.append(cube(i))
# print(newl)
 
# for i in l:
#     print(cube(i)) ye do tareeke hai jinse ham kar skte hai oeration lekin itna jada line of code likkhne se achha hai map 

newl  =  tuple(map(cube , l)); # ye list tuple sab kar skta hai return 
 
 
#  ===========map(function , iterable)===============

def filter_function(num):
    return num>6;
naylist = list(filter(filter_function , l));
print(naylist) #ye filter ki condition ko verify karke resulte karta h.

# ========================filter(function , iterable)==================================


 
# reduce bhi ek higher order function hai ise hame import karne ki jaroorat hoti hai
 
 
#   ==============================reduce(function , iterable)===============================
#  iska use tab karte hai jab single value chahiye hoti hai matlb ccumulataion and agreegation m iska use karte hai.
from functools import reduce

list = [1,2,3,4]; 
def sum(a,b):
    return a+b;
print(reduce(sum , list));



# map sabhi element par ek function apply karta hai
# filter condition ke basis per element ko select ya filter karta hai.
# reduce single value return karta h only 