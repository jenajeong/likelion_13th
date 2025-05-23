class Parent:
    def __init__(self):
        self.message = "Hello from Parent class!"

    def hello(self):
        print(self.message)

    @classmethod
    def this_is_class_method(cls):
        print("This is a class method!")


p = Parent()
p.hello()  # Output: Hello from Parent class!

Parent.this_is_class_method()  # Output: This is a class method!
