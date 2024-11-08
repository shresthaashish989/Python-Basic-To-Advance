#in python there are two type of function 
#1. built-in function
#2. user defined function
#built-in function are the function which are already defined in python library
#example of built-in function are print(),len(),type(),range(),max(),min()
#user defined function are the function which are defined by user

#no parameter mno retun type function
def hello():
    print("hello")

hello()

#paremeter but no return type
def hello(name):
    print("hello",name)

hello("vaskar")
hello("dipsesh")

def squre(number):
    print(f"the squre of the {number} is ",number*number)
squre(6)
#parameter and return type function
def add(a,b):
    sum=a+b
    return sum
c=add(2,4)
print(c)
print("the sum of the two number is ",add(20,40))

              






    
    