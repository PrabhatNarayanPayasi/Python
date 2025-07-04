#  there is no direct concept of access speciier in pthon.
# like other progrmming languages
# Python mein data ko access karne ka tareeqa thoda alag hai.
# Python mein jo main types of access control hote hain, wo kuch is tarah se work karte hain:


# public 

# in python if any  method or attribute is not starting with any special symbol
# then it is public 
# ham ise class ke bahr se easly access kar skte hai 
class Public:
    def show(self):
        print("Public")
a = Public();
a.show();

# protected 

# in python is any attribute or method is starting wiwth _(underscore)
# then it is protected.
# Yeh convention hai, jo sirf developer ko yeh batata hai ki yeh member
# internal use ke liye hai, lekin technically aap isay access kar sakte ho.
class Protected:
    def _protected(self):
        print("Protected");
b = Protected();
b._protected();

# private 

# in python if any attribute or method of the class is starting with 
# __(double underscore) then it is privvate .
# ise directly access nhi kiya ja skta access karne ke liye python name mangling 
# ka use karta hai.
class Private:
    def __private(self):
        print("PRivate")
c = Private();
c._Private__private(); # ye hoti hai name mangling 
# private ko access karne ke liye object._classNAme__methoName();

class P:
    def __p(self):
        print("Public 2");
d = P();
# d.__p() can  not be accessed directly.
d._P__p();  # can be accesed indirectly

# Yes, name mangling ke zariye outside the class aap private attributes aur methods ko access kar sakte ho, agar aap mangled name ko jante ho.
# Lekin, yeh practice bad hai, kyunki aap class ke internal details ko bypass kar rahe ho, aur aapke code ka maintenance mushkil ho sakta hai.
# Python mein private members ka use encapsulation ke liye hota hai, aur name mangling sirf unko accidental access se bachane ke liye hota hai