import random
comp = random.randint(0 , 2);
user = int(input("0 for snake, 1for water and 2 for gun"));
def check(comp , user):
    if(comp==user):
        return 0;
    if(comp==0 and user==1):
        return -1;
    if(comp==0 and user==2):
        return 1;
    if(comp==1 and user==2):
        return 1;
    if(comp==1 and user==0):
        return 1;
    if(comp==2 and user==0):
        return 1;
    if(comp==2 and user ==1):
        return 1;
    return 1;
       

score = check(comp , user)
if(score==0):
    print("Its draw");
elif(score==-1):
    print("Los")
else:
    print("Win");








'''

import random

def check(comp, user):
  if comp ==user:
    return 0
    
  if(comp == 0 and user ==1):
    return -1
    
  if(comp == 1 and user ==2):
    return -1
    
  if(comp == 2 and user == 0):
    return -1

  return 1
    
  
comp = random.randint(0, 2)
user = int(input("0 for Snake, 1 for water and 2 for Gun:\n"))

score = check(comp, user)

print("You: ", user)
print("Computer: ", comp)

if(score == 0):
  print("Its a draw")
elif (score == -1):
  print("You Lose")
else:
  print("You Won")
  

'''