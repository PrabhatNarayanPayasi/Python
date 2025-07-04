#  custom datatype bnane ke liye ham log classes ka use karte hai 
# class method ek special tareh ka method hai jo class level per operate hota hai na ki object level par 
# iska use class ki properties ko modify aur access karne ke liye kiya jata hai . 


# class method ko define karne ke liye @classmethod decorator ka use kiya jata hai
# class method ko pehla argument cls diya jata hai joki class ko represent karta hai cls ki jageh
#  aur kucch bhi likh skte hia lekin ye class ko represent 
# karta hai jaise object ya function me self dete hai . 
# class method ko ham class ke naam se bhi call kar skte hai yaa fir 
# class ke object ke through bhi . 
 
 
 
 
class Emp:
    company = "Apple"
    def show(self):
        print(f"the name is {self.name} and company name is {self.company}");
    @classmethod
    def change(cls , nCompany): # by default pehla argument as
        # an instance milta hai agar me @staticmethod decorator laga du to
        # pehla arg as an class mmil jayega fir ham class variable ko
        # change kar skte hai . 
        
          cls.company = nCompany;   
a = Emp();
a.name = "sl"
a.company = "Microsoft"
a.show();
a.change("TEsla");
a.show()
print(Emp.company);

# class method se directly class ke variable ya class ko change kar skte hai 
#  without classmethod decorator ke ye instance ke jaise work karti hai 

# jo class method hota hai usse class level ke variable ko cchange ya access karte hai 
# iske liye hame @classmethod decorator ka use karna hota hai 
# isse ham seedhe class variable ko change kar skte hai 
# jaise code ikhe hai hum to agar @classmethod decorator ko nhi use karenge 
# to change function me jo cls h vo as a instance ban jayega aur company name class level per change nhi ho payega 
# isi liye class method ka use karte hai . 
# matlb cls class ko refer karta hai aur self object ko 