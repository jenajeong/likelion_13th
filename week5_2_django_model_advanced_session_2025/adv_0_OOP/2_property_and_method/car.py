class Car:
    def __init__(self, 이름, 색상, 생산연도, 속도=0):
        self.이름 = 이름 # 자동차 이름
        self.색상 = 색상 # 자동차 색상
        self.생산연도 = 생산연도 # 자동차 제조 연도
        self.속도 = 0 # 자동차의 현재 속도
    
    def 출발(self):
        self.속도 = 10
        print("부릉부릉!")

    def 가속(self):
        self.속도 += 10
        print(f"가속 중입니다! {self.속도}km/h로 달리고 있습니다.")

    def 정지(self):
        self.속도 = 0
        print("정지했습니다.")

if __name__ == "__main__":
    람보르기니 = Car("Lamborghini", "yellow", 2023)
    페라리 = Car("Ferrari", "red", 2022)

    print(람보르기니.이름, 람보르기니.색상, 람보르기니.생산연도)
    print(페라리.이름, 페라리.색상, 페라리.생산연도)

    람보르기니.출발()
    람보르기니.가속()
    람보르기니.가속()
    람보르기니.정지()
    print(람보르기니.속도)
