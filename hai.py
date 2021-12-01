class Hi:
    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
           raise TypeError('Hi must be a string')
        else:
           self.__name = value

    def greeting(self):
        print(f'Hi, {self.name}')

    def __repr__(self):
        return 'Hi =  Hello, A word for greeting'


