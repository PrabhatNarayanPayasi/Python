#  time module ek built in module hia python me 
#  jo time related task ko poora karne ke liye
#  different functions ka use karta hai . 
#  1) time() : ye time ko seconds me return karta hai . 
# jo unix epoch se leke ab tak ka time  hai 
#  unix epoch matlb (197 , january 1) 
import time
# t = time.time()
# print(t);

# 2) sleep() : ye ek argument leta hai second ki form me aur utene
#  second tak hi program ko rok ke rakh leta hai jitna ise diya gya hai 
# print(4);
# time.sleep(4);
# print("Time Overed")

# 3) localtime() :ye function current local time karta hai
#  leki us country ke local time ko btaata hia 
# jaha aapka code editor run kar rha hota hai . 
# ye struct_time obj return karta hai
# print(time.localtime())



# 3) strftime() :  ye date aur time ko standered formate me print
# karta hai . 
# import time

# current_time = time.localtime()  # Local time
# formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", current_time)
# print(formatted_time)  # Example Output: 2025-02-23 15:45:30


# 4) gmtime() :  ye function time ko UTC(universal time coordinate) me 
#  convert karta hai aur struct_time object ko return karta hai .
# time = time.gmtime();
# print(time)

# 4) mktime : ye funtion struct_time object ko second me convert karta hai
# print(time.mktime(time.localtime())) # ye ek argument leta hai tabhi to use seconds me convert kar pata hai
#  ye kisi specific date ke time ko second me conert karne ke liye hota hai 
#  jabki ham time.time(0 se since 1970 , 1 january vale tim ko seconds me converts kar skte hia )

print(time.time());
print(time.mktime(time.localtime()))


'''
matlb m ye bolu ki time.time() to epoch time deta hai 
ab tak ka second me ji country m ye bna tha aur 
time.mkime(time.localtime()) 
epoch time se ab tak ka time deta hai jis c
country m coderun ho rha hai 
'''



# 7) perf_counter():
# Yeh function high-resolution timer ko return
# karta hai, jo performance measurement ke liye useful
# hota hai. Iska use aap code ke execution time ko 
# measure karne ke liye kar sakte hain.
 
#
import time

start_time = time.perf_counter()
# Code to be measured
time.sleep(2)  # Simulate delay
end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"Execution Time: {execution_time} seconds")


 