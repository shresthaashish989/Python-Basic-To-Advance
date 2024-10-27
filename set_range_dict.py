# in this set datatypes we can add and remove the data from set buct cant be slice and indexing

s={10,20,30,40}
s.add(50)
print(s)
s.add(60)
print(s)
print(type(s))


# we cant add and remove any kind of data
fs=frozenset(s)
print(fs)
print(type(fs))



#dict or dictionary we need to key and value for dict
#dict is mutable
#dict is unordered collection of key and value pair

d={300:'dipesh',400:'ashish',500:'appex'}

print(d)
print(type(d))
d[600]="kamala"
d[300]="princess"
print(d)

#range
#range is immutable
#range is a sequence of numbers
#range is used for loop
#range is used for iteration
r=range(20,10,-2)
print(r)
for i in r:
  print(i)


ra=range(10,20,2)
print(ra)

print(ra[0])





