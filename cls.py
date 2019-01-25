class Site:
    def __init__(self, name, url):
        self.name = name
        self.__url = url

    def who(self):
        print('name :', self.name)
        print('url :', self.__url)

    def __foo(self):
        print('This is private')

    def foo(self):
        print('This is public')
        self.__foo()


x = Site('Gu', 'jianhong.gu@Key.com')
x.who()
x.foo()
x.__foo()
