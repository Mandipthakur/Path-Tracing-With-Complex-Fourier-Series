from jarvis.modulec import *

class A(C):
    def __init__(self):
        print dir(self.__class__)
#        print id(self.__class__.__bases__[0])
#        self.__class__.__base__ = C
        print id(self.__class__.__base__)
        super(A, self).__init__()
