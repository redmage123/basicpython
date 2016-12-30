#!/usr/bin/env python

class Restaurant(object):

    def __init__(self,**kwargs):
        self.name = kwargs["name"]
        self.rank = kwargs["rank"]



    def __str__(self):
        return "Restaurant %s has ranking %d" % (self.name,self.rank)


    def __cmp__(self,other):
        if (self.rank < other.rank):
            return -1
        elif (self.rank == other.rank):
            return 0
        else:
            return 1




r1 = Restaurant(name="Alice's Restaurant",rank=3)
r2 = Restaurant(name = "Bob's Grill",rank=2)


if (r1 > r2): 
    print "Alice's is the best"
else:
    print "Bob's is the best"
