# 실습1
#name = input('이름을 입력하세요: ')
#age = int(input('나이를 입력하세요: '))
#height = float(input('키를 입력하세요: '))

#print('나이: ', age)
#print('키: ', height)
#print('이름: ', name)




#실습2

#score = int(input('점수를 입력하세요: '))
#if score >=90:
#    print('A')
#elif score >=80:
#    print('B')
#elif score >= 70:
#    print('C')
#elif score >= 60:
#    print('D')
#else:
#    print('F')




#실습3-1
#n = int(input('숫자를 입력하세요: '))
#sum=0
#for i in range(1, n+1):
#    sum+=i
#print(sum)




#실습3-2
#n = int(input('숫자를 입력하세요: '))
#result = 0
#count = 1

#while count <=n:
#    result+=count
#    count +=1
#print(result)



#실습4
#def max_number(a,b):
#    if a>b:
#        return a
#    else:
#        return b

#a = int(input('첫 번째 숫자를 입력하세요: '))
#b = int(input('두 번째 숫자를 입력하세요: '))

#print('큰 수: ', max_number(a,b))




#실습5
class Car:
    def __init__(self, name):
        self.name= name
        self.speed = 0
        
    def showinfo(self):
        print('차 이름: ', self.name)
        print('차 속도: ', self.speed)
    
    def accelerate(self):
        self.speed +=10
    
    def brake(self):
        if self.speed >= 10:
            self.speed -= 10
        else:
            self.speed = 0

          
car = Car("람보르기니")
car.showinfo()
car.accelerate()
car.showinfo()
car.brake()
car.showinfo()
car.brake()
car.showinfo()
        
