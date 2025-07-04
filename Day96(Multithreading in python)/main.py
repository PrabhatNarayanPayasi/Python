#  python m multithreading ka matlab hota hai ki
#  ek hi program ko multuple threads ke through parellel
#  execute kiya ja ske . 

#  har thread ek doosre se independent hota hai isme 
# isse prograam ki performance improove hoti hai . 
#  especially jab tasks independent ho aur unko 
#  parellel process kiya ja ske . 

#  multi threading multiple task ko karne ke liye hota hai . 
# ye mainly  tab use hota hai jab prograam ke different different task 
#  ek doosre se related na ho 
#  ye I/O bound operation jaise ki file reading , web requests , database access etc . ko parellel executr karne m kaam aata hai . 




#  python me
# multithreading ka use karne ke 
# liye threading module ka use kiya 
#  jata hai 

# import threading
# import time
# def number():
#     for i in range(1,6):
        
#         print(i)
#         time.sleep(1);
# def letter():
#     for l in ["A" , "B" , "C" , "D" , "E"]:
#         print(l);
#         time.sleep(1);
# t1 = threading.Thread(target=number);
# t2 = threading.Thread(target=letter);

# t1.start();
# t2.start();

# t1.join()
# t2.join()

# python ka interpreter GIL(Global Interpretor Lock) ka 
# use  karta hai . Iska matlb hai h ki 
#  ek waqt pe sirf ek hi thread cpu ko use kar skta hai 
#  isliye CPU bound task me Multithreading ka utna benifecial use nhi ho pata hai . 

# I/O bound task me multithreading ka use kaafi benificial hai . 


'''
1. I/O-bound Tasks:
I/O-bound tasks woh tasks hote hain jinmein input/output operations involve hote hain, jaise disk operations, network requests, ya database queries. In tasks ko execute karte waqt, program ka zyada waqt waiting mein jata hai jab tak data read ya write nahi hota ya network response nahi milta.

Examples of I/O-bound tasks:

File system operations (jaise file read/write)
Network requests (jaise web scraping, API calls, etc.)
Database operations
User input/output in interactive applications
'''


'''
 CPU-bound Tasks:
CPU-bound tasks woh tasks hote hain jo CPU resources ka use karte hain, jaise complex calculations, mathematical computations, ya data processing. In tasks mein program ka zyada waqt CPU ko use karne mein jata hai aur yeh tasks parallel execution ka fayda utha sakte hain agar unhe multiple threads mein divide kiya jaye.

Examples of CPU-bound tasks:

Data analysis, mathematical modeling
Image processing, video encoding
Sorting large datasets
Cryptography, complex simulations
'''




'''
Multithreading CPU-bound tasks ke liye efficient nahi hoti Python mein, kyunki GIL ek time pe sirf ek thread ko allow karta hai bytecode execute karne ke liye, jo parallelism ko limit karta hai.
Agar aapko true parallelism chahiye for CPU-bound tasks, toh multiprocessing ka use karna chahiye, jisme har process apne alag CPU core pe run karta hai aur GIL ka effect nahi hota.
'''
import threading
import time
def time1():
    for i in range(5):
        print(i);
        time.sleep(1);
def ch():
    for i in ["a" , "b" , "c" , "d"]:
        print(i);
        time.sleep(1);

t1 = threading.Thread(target=time1);
t2= threading.Thread(target=ch);
t1.start();
t2.start()

'''
threading module mein .join() ka use is liye kiya jata hai taake ek thread ko complete hone tak wait kiya ja sake. Jab multiple threads ek sath kaam kar rahe hote hain, to agar aap chaahte hain ke main thread ya parent thread tab tak apna kaam na kare jab tak saare threads apna kaam complete nahi kar lete, tab .join() ka istemal kiya jata hai.
'''




'''
Thread ek chhota unit hota hai jo ek
process ke andar execute hota hai. 
Aap isse ek tarah se "sub-process" bhi 
samajh sakte hain. Threads ka use parallel
execution ko manage karne ke liye kiya 
jata hai, taaki multiple tasks ek saath 
chal sakein, bina ek dusre ko interfere 
kiye.

Threading ka basic concept:
Jab aap kisi program ko run karte hain, to wo ek process create karta hai. Har process mein kam se kam ek thread hota hai, jo ki code execute karta hai.

Agar aapko ek process ke andar ek se zyada kaam (tasks) parallelly execute karne hain, to aap multiple threads create kar sakte hain. Har thread independently kaam karta hai aur ye parallelly ek hi process ke andar chal rahe hote hain.
'''