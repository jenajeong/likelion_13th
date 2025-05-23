#print문
#print('정제나')



#input함수
#name = input("이름을 입력하세요: ")
#student_number = input('학번을 입력하세요: ')
#print("이름: ", name)
#print("학번: ", student_number)



#조건문
#num = int(input('숫자를 입력하세요: '))
#if num >0:
#    print('양수입니다')
#elif num <0:
#    print('음수입니다.')
#else:
#    print('0 입니다.')
 
 
    
#반복문
#n = int(input('n을 입력하세요: '))

#print('for문 출력문')
#for i in range(1,n+1):
#    print(i)
#print()

#print('while문 출력문')
#count = 1
#while count <= n:
#    print(count)
#    count+=1



#def 함수
#def add(a,b):
#    return a+b

#def sub(a,b):
#    return a-b

#def mul(a,b):
#    return a*b

#def div(a,b):
#    return a/b

#num1 = int(input("첫 번째 숫자를 입력하세요: "))
#num2 = int(input("두 번째 숫자를 입력하세요: "))

#print('덧셈: ', add(num1, num2))
#print('뺄셈: ', sub(num1, num2))
#print('곱셈: ', mul(num1, num2))
#print('나눗셈: ', div(num1, num2))

#클래스

class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result +=num
        return self.result
    def sub(self, num):
        self.result -=num
        return self.result
    def mul(self, num):
        self.result *= num
        return self.result
    def div(self, num):
        self.result /= num
        return self.result
    
cal = Calculator()

print(cal.add(3))
print(cal.sub(1))
print(cal.mul(3))
print(cal.div(2))