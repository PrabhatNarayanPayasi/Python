#  generators ka use hota hai on the fly values ko generate karne ke liye. 

#  ye special type of function hote hai . jo ki generate object return karta hai
# ye generator object special isliye hota hai kyoki ye value ko stor karke nhi rakhta hai lekin 
# ye us information ko stor karke rakhta hai jisse value ko bnaya ja skta hai on the fly instantly


#  ye best tools h python me for workin with large database or infinitesequence of data 
#  ye use hote h vaha jaha hame entire sequence ya data ko store karna nhi hota 
# ye memory efficient hote hai aur hamare program ki efficieancy ko badhate hai . 






#  Generator lazy computations kause karte hai . 
#  matlb ye on demand value ko generat karte hai .
# generator functions ko aap kisi sequence ya collection ka data step by step 
#  generat karne ke liye use karte hai 
#  poori sequence ko ek hi baar m bina load kiye 


'''
Key Points About Generators:
Lazy Evaluation: Generator values ko ek-ek karke calculate karta hai jab unhe zarurat padti hai. Matlab, woh sequence ko ek baar mein memory mein store nahi karta.
Efficient Memory Usage: Kyunki generator ek time par ek hi value generate karta hai, isliye memory ka usage bahut kam hota hai.
Stateful: Jab generator function call hota hai, toh woh apni state ko maintain karta hai aur har baar usse value generate karne pe state ko update karta hai.
'''




#  generaors functions ko yeild keyword se ddefine kiya jata hai 
#  jb kisi computaion me program flow yeild keyword tak pahuch jata hai 
#  to execution pause ho jate hai aur stored value retur ho jati hai .



# def name():
#     yield 1;
    
# n = name();
# # print(next(name()))
# print(name()) # ye ek generator object return karega aur uski location bhii . 



#   agar ham next ka use karte hai to ye ek ek item ko next call per return karega 


# def MyZ():
#     yield 1;
#     yield 2;
#     yield 3;
#     yield 4;
# z = MyZ();
# print(next(z))
# print(next(z))

#  bina next ke bhi value ko print karva skte hai 
# for loop basically iterate karta hai function m 
#  yield ki value ko
#  
# def simple_generator():
#     yield 1
#     yield 2 # iska main use vaha hota hai jaha hame values ko ek time per ek hi 
#     #  generate arne ki jaroorat hoti hai . 
#     yield 3

# # Generator ko for loop ke through iterate karna
# for value in simple_generator():
#     print(value)



def MyZ():
    for i in range(5):
        yield i;
mz = MyZ();
# print(next(mz))
for i in mz:
    print(i)  # yaha par bhi value ek ek karke hi print ho rhi hai lekin fast execution ke karan 
    #  hame fast looping ke karan pata nhi chal pata hai .
    