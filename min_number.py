a=int(input("enter a first number:"))
b=int(input("enter a second number:"))
min=a if a<b else b
print("minimum number is:",min)


#minimum of three numbers
a=int(input("enter a first number:"))
b=int(input("enter a second number:"))
c=int(input("enter a third number:"))
minmum=a if a<b and a<c else b if b<c else c
print("minimum number is:",minmum)