#!/usr/bin/env python


class baseclass1():
    def __init__(self,att1,att2):
        self.att1 = att1
        self.att2 = att2
        print "Calling baseclass1's init function"


class baseclass2(baseclass1):
    def __init__(self,att1,att2,att3):
        baseclass1.__init__(self,att1,att2)
        self.att3 = att3
        print "Calling baseclass1's init function"


class derivedclass(baseclass2):

    def __init__(self,att1,att2,att3,att4):
        baseclass2.__init__(self,att1,att2,att3)
        self.att4 = att4
        print "Calling derivedclass1's init function"


myclass = derivedclass("fee","fi","fo","fum")
