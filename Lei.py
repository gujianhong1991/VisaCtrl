class Parent:
    def myMethod(self):
        print('Parent Class')


class Child(Parent):
    def myMethod(self):
        print('Child Class')


c = Child()
c.myMethod()
super(Child, c).myMethod()
