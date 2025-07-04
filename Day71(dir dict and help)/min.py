x=[1,2,3]
print(dir(x))
print(x.__lt__)
#  dir method kisi class ke attribute ya objec ke method ko dekhne ke liye use
# kiya jata hai jab bina kisi argument ke ke call kiya jata hai to 
# ye us object ke sabhi identifier ko show kar deta hia 
# lekin jab ise koi argument diya jata hai to ye keval usi argument ke
# us perticular method ko bas dikhata hai 


# dict method ka use dictionary object bnane ke liye kiya jata hai 
# ye unorderd pair hota hai . isme key value pair hote hai 
# iska use ham kisi iterable ko dictionary me convert karne ke liye bhi 
# kar skte hai .
x1 = dict(name="prabhat"); 
print(type(x1))



# help method ka use kisi bhi function attribute ya obj ki documentation dekhne ke liye kiya jata hai 
# isse function ke usesaur uski functionality ke bare me detailed information milti hai 
# help(str)
help(len)