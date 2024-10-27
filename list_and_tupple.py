a=[10,20,30,40,50,10,30,20,10,"hellow",10.4,10+3j ]
print(a)

#if we need to find type of variable datatype
print(type(a))

#if wee need a a specific list 
print(a[2])

# if we need to 30 and 40 
print(a[2:4])

#we need to add value in this list 
a.append(100)
print(a)
a.remove(20)
print(a)
a[1]=120
print(a)

for x in a:
    print(x)

#tupples is immutable but same as list

t=(10,30,40,100,50)
print(type(t))