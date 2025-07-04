#  walrus operator python 3.8 me introduce kiya  gya hai 
#  iska naam Assignment operator bhi hai 
#  iska primary purspose ek expression ke ander variable ko assign karna hai aur 
#  resulte ko ek hi line me print karna hai . 



#  Syntax :
# variable := expression

#  iski need isliye padi hai 
# 1) code ko readability aur cocncise banana;
# 2) Looping efficiency 

#  WIthout Walrus operator : 
# value = input("Enter your choice");
# while(value != "quit"):
#     print("Enter again");
#     value = (input("Enter gain value : "));
    # isme hamne apne value variable ko pehle input se value li 
    #  phir input call hua to value assign hui fir condition check hui
    #  fir dobara se agar condition match nhi hui to input call ho rha hai
    #  to yaha pe loooping ka kam ho trha hai 
    
#   With Walrus operator :
# while(value :=input("Enter value") !="quit"):
#     print("Enter value again")
    
# n = int(input("Enter n : "));
# while(n!=4):
#      print("not equal")
#      n=  int(input("Again"));
while(n := int(input("N : "))!=4):
    
    print("again")