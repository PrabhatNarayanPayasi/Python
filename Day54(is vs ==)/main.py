# is and == dono comparision operator hi hote hai.
# difference ye hota hai ki is compare karta hai exact location of the variable ko and 
# == compare karta hai value ko only.
a=4
b="4"
#print(a is b); #exact location of object in memory
#print(a==b); #value

c=[1,2,3,4]
d=[1,2,3,4]
print(c is d);
print(c==d)

x=3;
y=3;
print(x is y);
print(x==y)
# jab python me ham constant bnate hai jaise x=3 to ye memory location me ek baar banta hai
# python const ko change na karke space waste nhi karta hai
# matlb jo jo cheej imutable hai unnke liye python true return karega.
