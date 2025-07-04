# jab bhi ham ek se jada inheritance use karte hai 
# to usko bolte hai 
# hybrid inheritance . 
class Base:
    pass
class Derived1(Base):
    pass
class Derived2(Base):
    pass
class Derived3(Base , Derived1):
    pass


#  hirericle inheritance is a type off inheritance where multiple subclasses inherit
# single base class . 
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B):
    pass
