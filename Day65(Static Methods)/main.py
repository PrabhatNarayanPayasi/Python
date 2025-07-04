# static methods vo methods hote hain jo na to class
# ko belong  karte hai aur na hi instance ko belong karte hai
# static method ka use karne se class ka object bnane ki jaroorat nhi padti
# directly class ka name .method call kar skte hai ham


class Math:
    def add(self  , b , a):
        return b+a;
a = Math();
print(a.add(4 , 6 ))

class Math2:
    @staticmethod
    def add2(a , b):
        return a+b;
print(Math2.add2(6,8));
# Haan, static method mein self keyword ki zarurat nahi padti, aur na hi aapko cls ki zarurat hoti hai.

# Static Method mein self ka use nahi hota kyunki:
# self instance (object) ko refer karta hai, aur static method class ke kisi bhi instance (object) se related nahi hoti.
# Static method ka kaam hota hai ki woh class level pe kaam kare, bina kisi specific object ya instance ke.





'''

static method class level per hoti hai ise bina class object ke use kiya j skta hai
ise use karne ke liye @staticmethod ka use kiya jata hai . 


'''