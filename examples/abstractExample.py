#!/usr/bin/python3

from abc import ABCMeta, abstractmethod


class abstractExample(metaclass=ABCMeta):
    
    def __init__(self):
        pass

    @abstractmethod
    def method1(self):
        return

    @abstractmethod
    def method2(self):
        return


class concreteExample(object):
    def __init__(self):
        self.foo = "foo"
        self.bar = "bar"


    def method1(self):
        return(self.foo)

    def method2(self):
        return(self.bar)

abstractExample.register(concreteExample)

if __name__ == '__main__':
    c = concreteExample()
    print (c.method1())
    print (c.method2())

