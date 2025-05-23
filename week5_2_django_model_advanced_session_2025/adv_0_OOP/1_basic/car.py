class Car:
    def __init__(self, 이름, 색상, 생산연도, 속도=0):
        self.이름 = 이름 # 자동차 이름
        self.색상 = 색상 # 자동차 색상
        self.생산연도 = 생산연도 # 자동차 제조 연도
        self.속도 = 0 # 자동차의 현재 속도


if __name__ == "__main__":
    람보르기니 = Car("Lamborghini", "yellow", 2023)
    페라리 = Car("Ferrari", "red", 2022)

    print(람보르기니.이름) # Lamborghini
    print(람보르기니.색상) # yellow
    print(람보르기니.생산연도) # 2023
    print(람보르기니.속도) # 0
