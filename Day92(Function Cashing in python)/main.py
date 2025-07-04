# cache :-  ek temporary storage hai jaha pe ham
# pehle se computed resulte ko store karke rakhte hai 



# cashing ka fayda ye h ki ham repeated  computation ko avoid karte hai 
# aur program ko fast bna dete hai 


#  ab python me cashing ko manage karne ke liye ham functools.lru.cache ka use karte hai
# jo ki ek built in tool hai jo cashing ko automatically manage karte hai . 




# Maan lo tumhare paas ek function hai jo kisi number 
# ke square ka result de raha hai. Agar tum baar-baar same number ke square ka result
# chahte ho, toh har baar computation karne ki bajaye, hum pehle se computed result ko 
# cache (ya store) kar sakte hain.

'''
thon mein caching ka matlab hota hai kisi data ko temporarily store kar lena taake jab usi data ki dobara zarurat pade, toh usay phir se process na karna pade, aur hum jaldi se result le sakein.

Iska basic idea yeh hai ke jab hum ek 
kaam baar-baar kar rahe hote hain, toh 
uss kaam ko repeat
karne ki bajaye, hum pehle se jo result 
mila tha, usse dobara use kar lete hain.
Yeh humare program ko fast bana deta hai . 
'''

#  cache using dictionary
import time
cache = {};
def square(num):
    if num in cache:
        print(f"using cache resulte is : {cache[num]}")
    else:
        time.sleep(2)
        res = num*num;
        cache[num] = res;
        print(res)
# square(5)
# square(6)
# square(53)
# square(6)
# square(51)
# square(5)

#  yaha par hamne dictionary ka use karke cache ko
#  manage kiya hai basic matlb ye  hai ki ham
#  cache me resulte ko store karva ke rakhte hai pehle 
#  fir usko return krva dete hai 


# ==================Cache using Built in Module ==============================

from functools import lru_cache
import time

@lru_cache(maxsize=None)  # No limit on cache size
def squ(num):
    time.sleep(2)  # Simulating a slow function
    print(num * num)  # Printing the result

squ(3)  # Printing 9 (takes time)
squ(3)  # Printing 16 (takes time)
# squ(5)  # Printing 25 (takes time)
# squ(6)  # Printing 36 (takes time)
# squ(4)  # Printing 16 (cach2ed, no delay)
#  is vaale code me last me jo squ(4) hai 
# vo print nhi hota hai iska main reason ye hai ki
#  lru cache returned/cached value ko store karke rakhta hai only
#  print function resulte ko return nhi karta hai isliye 

# from functools import lru_cache
# import time

# @lru_cache(maxsize=None)  # No limit on cache size
# def squ(num):
#     time.sleep(2)  # Simulating a slow function
#     return num * num  # Return the result, not print

# print(squ(3))  # 9 (takes time)
# print(squ(4))  # 16 (takes time)
# print(squ(5))  # 25 (takes time)
# print(squ(6))  # 36 (takes time)
# print(squ(4))  # 16 (cached, no delay)






'''
    iska matlb m ye bolu ki lru cache keval unhi values ke sath effect karta hai jab koi value return ho rhi ho agar hm value ko return nhi kar rhe hai h aur lru cache ka use bhi kar rhe hai aur agar do baar same kaam karvaya jai square(3) and square(3) to keval ek hi baar print hoga square 
ChatGPT said:
Haan, aap bilkul sahi samajh rahe hain!

lru_cache tabhi kaam karta hai jab function return value de raha ho. Agar aap print() kar rahe hain, toh woh value ko return nahi karte, isliye lru_cache ka effect nahi hoga.'''