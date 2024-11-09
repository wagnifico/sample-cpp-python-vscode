

# from ctypes import cdll
# lib = cdll.LoadLibrary('libclass.so')

import ctypes
import os

# modyfying the path at the load time seemsto not work
# https://stackoverflow.com/a/64472088
# https://stackoverflow.com/a/52408140
libpath = f'{os.path.dirname(os.path.abspath(__file__))}/build/libclass.so'
lib = ctypes.CDLL(libpath,mode=ctypes.RTLD_GLOBAL)



class DummyClass:
    def __init__(self):
        self.obj = lib.DummyClass()

    def sayHelloFromCode(self,b):
        lib.sayHelloFromCode(self.obj,b)

    def sayHelloFromHeader(self,b):
        lib.sayHelloFromHeader(self.obj,b)

