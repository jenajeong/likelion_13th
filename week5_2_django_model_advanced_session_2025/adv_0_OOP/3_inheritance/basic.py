class Parent:
    def __init__(self):
        self.message = "Hello from Parent class!"

    def likelion(self):
        print("likelion")

    def hello(self):
        print(self.message)

    def move(self):
        print("moving!")

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.message = "Hello from Child class!"

    def move(self):
        print("moving in Child class!")


parent = Parent()
parent.likelion()  # Output: likelion
parent.hello()  # Output: Hello from Parent class!
parent.move()   # Output: moving!

child = Child()
child.likelion()  # Output: likelion
child.hello()   # Output: Hello from Child class!
child.move()    # Output: moving! moving in Child class!
