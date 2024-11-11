#class and object
# In this example, you’ll see how to create and interact with Student objects. After defining
# the Student class with attributes like name, and grade,


class student:
    def __init__(self,name, grade):
        self.name = name
        self.grade = grade
    def info(self):
        return f"name is {self.name} and grade is {self.grade}"
    def passed(self):
        if self.grade>=60:
            return (f"congratulation {self.name} you are pass ")
        else:
            return (f"please try again ")
        
#object
s1 =student("hari",90)
s2 =student("gita",50)
s3 =student("krishna",20)

print(s1.info())
print(s2.info())

print(s1.passed())
print(s2.passed())
print(s3.passed())


 #Write a Python program to create a class Laptop with the properties id, name, and ram. Then,
# create three objects of this class and print all their details.
class laptop:
    def __init__(self,brand,price,ram):
        self.brand=brand
        self.price=price
        self.ram=ram
    def info(self):
        return (f"brand is {self.brand} and ram is {self.ram}")
    def check_price(self):
        if self.price>90000:
            return (f"laptop is expensive {self.price}")
        else:
            return (f"laptop is cheap {self.price}")
        

l1=laptop("dell" ,80000, "8gb")
l2=laptop("Accer",120000,"12gb")
l3=laptop("Aspire",60000,"4gb")

print(l1.info())
print(l1.check_price())


