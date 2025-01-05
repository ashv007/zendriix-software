# class Person:
#     def __init__(self,first_name,last_name,age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
# p1 = Person('Ashwani','Vishwakarma',22)
# print(p1)
class Laptop:
    def __init__(self,brand_name,model_name,price):
        # instance variable
        self.brand  = brand_name
        self.name = model_name
        self.price = price
        self.laptop_detail = brand_name +' '+ model_name
    def apply_discount(self,num):
        #self.price
        off_price = (num/100)*self.price
        return self.price - off_price

p1 = Laptop('Lenovo','i3 gen',30000)
print(p1.apply_discount(20))