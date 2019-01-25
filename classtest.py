# class peo:
#     def __init__(self, name, age, sex):
#         self.Name = name
#         self.Age = age
#         self.Sex = sex
#
#     def speak(self):
#         print("my name" + self.Name)
#
#
# class info(object):
#
#     @classmethod
#     def sayclassmethod(cls):
#         print('say %s' % cls)
#
#     def saymethod(self):
#         print('say %s' % self)
#
#
# test = info()
# test.saymethod()
# test.sayclassmethod()
# info.saymethod(test)
# info.sayclassmethod()


class people:
    name = ''
    age = 0
    __weight = 0

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s said it is %d years old" % (self.name, self.age))


class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        people.__init__(self, n, a, w)
        self.grade = g

    def speak(self):
        print("%s said it is %d years old, %d grade" % (self.name, self.age, self.grade))


s = student('ken', 10, 60, 3)
s.speak()
