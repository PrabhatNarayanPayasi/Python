'''hour =  int(input("Enter time in hour"))
if(hour >=0 and hour<12):
    print("Good Morning Sir");
elif(hour>=12 & hour<17):
    print("Good AfterNoon Sir");
elif(hour>=17 & hour<20):
    print("Good Evening Sir");
else:
    print("Good Night Sir");'''
    
    
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)


times = time.strftime('%H:%M:%S');
print(times)
t = int(time.strftime('%H'));
print(t)
if(t>0 & t<12):
    print("Good morning sir");
elif(t>12 & time<5):
    print("Good Afternoon sir");
elif(t>17 & time<20):
    print("Good Night Sir");
else:
    print("Good Night Sir . ");