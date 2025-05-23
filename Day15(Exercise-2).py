# apple= int(input("Enter appleprice"));
# budget = int(input("Enter budget : "));
# if(budget-apple > 200):
#     print("200 Bache hai");
# else:
#     print("200 bhi nahi bache . ");    200


# -----------------------------------------------------el - if ---------------------------------------------------------------------------------



# num = int(input("Enter the value of num : "));
# if(num>0):
#     print("Num is greater than 0");
# elif(num==0):
#     print("Num is equal to 0 . ");
# elif(num==-200):
#     print("Num is equal to 200 . ");
# else:
#     print("May be number is negative . ");


# -------------------------------------------------------nested-if----------------------------------------------------------------------------


# number = int(input("Enter number : "));
# if(number>0):
#     if(number<=10):
#         print("Under 10");
#     elif(number>10 and number<20):
#         print("Between 10 and 20 . ");
#     else:
#         print("Number is greater than 20");
# else:
#     print("Number is negative . ");

'''n =int(input("Enter the number : "));
if(n>0):
    print("Number is positive.");
elif(n==0):
    print("number is 0.");
else:
    print("Number is negative.");'''
    
    
'''a = int(input("Enter value of a : "));
b = int(input("Enter value of b :"));
if((a+b)>200):
        print("sum is greater than 20 ");
elif((a+b)==200):
        print("Sum is 200");
else:
    print("SUm is Greater than 200");'''
    
    

'''a = str(input("Enter"))
if(a=="Prabhat"):
    print("a is " + a);
elif(a=="Shiva"):
    print("a is shiva ");
else:
    print("a is not5 both of them ");'''
    
    
    
    
''' 
Excersice 2: Good Morning Sir
Create a python program capable of greeting you with Good Morning,
Good Afternoon and Good Evening.
Your program should use time module to get the current hour.
 
'''
# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
#  



import time
currtime= time.strftime('%H:%M:%S');
print(currtime)
print(time.strftime('%H'))
print(time.strftime('%M'))
print(time.strftime('%S'))