class Calculaor:
    num=100
    def __init__(self,a,b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executng as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculaor.num
        

obj =Calculaor() 
obj.getData()
print(obj.num)