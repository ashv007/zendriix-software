# inheritence is nothing but inherit th property of perent class
 
from OpsDemo import Calculaor

class ChildImp1(Calculator): 
    num2=200

    def __init__(self):
        Calculaor.__init__(self,2,10)



    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()
obj = ChildImp1()
print(obj.getCompleteData())
