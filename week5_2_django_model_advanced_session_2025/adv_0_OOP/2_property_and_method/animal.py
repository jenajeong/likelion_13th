class Animal:
    def __init__(self, 이름, 나이, 속도=0):
        self.이름 = 이름
        self.나이 = 나이
        self.속도 = 속도
    
    def 출발(self):
        self.속도 = 5
        print(f"{self.이름}가 출발했습니다.")
    
    def 가속(self):
        self.속도 += 5
        print(f"{self.이름}가 가속 중입니다! 현재 속도: {self.속도}km/h")
      
    def 정지(self):
        self.속도 = 0
        print(f"정지했습니다.")
    
if __name__ == "__main__":
    고양이 = Animal("고양이", 2)
    강아지 = Animal("강아지", 3)

    print(고양이.이름, 고양이.나이)
    print(강아지.이름, 강아지.나이)

    고양이.출발()
    고양이.가속()
    고양이.가속()
    고양이.정지()
    print(고양이.속도)
