#Overriding

class parent:
    def __init__(self):
        self.message = "parent"
    
    def one(self):
        print('1')
    
    def two(self):
        print('2')
        
class child(parent):
    def __init__(self):
        super().__init__()
        self.message = 'child'
    
    def one(self):
        print('one')

c = child()
print(c.message)
c.one() # 오버라이딩
c.two() #상속
        
#Overloading
# 없는 이유 : 오버로딩을 위해선 타입이 필요 -> 파이썬에선 각 변수들의 타입이 지정되어 있지 않기 때문에 불가능능

