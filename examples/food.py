#!/usr/bin/env python
class Food(object):
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories
    def tastesLike(self):
        raise NotImplementedException("Subclasses are responsible for creating this method")
                                         
class HotDog(Food):
    def __init__(self,name,calories):
        super(HotDog,self).__init__(name,calories)

    def tastesLike(self):
        return "Extremely processed meat" 
                                         
class Hamburger(Food):
    def __init__(self,name,calories):
        super(Hamburger,self).__init__(name,calories)
        self.foo = "foo"

    def tastesLike(self):
        return "grilled goodness" 
                                                                         
class ChickenPatty(Food):
    def __init__(self,name,calories):
        super(ChickenPatty,self).__init__(name,calories)
        self.foo = "foo"

    def tastesLike(self):
        return "tastes like chicken" 
                                                                                         
dinner = []
dinner.append(HotDog('Beef/Turkey BallPark', 230))
dinner.append(Hamburger('Lowfat Beef Patty', 260))
dinner.append(ChickenPatty('Micky Mouse shaped Chicken Tenders', 170))
                                                                             
# even though each course of the dinner is a different type 
# we can process them all in the same loop 

for course in dinner:
    print course.name + " is type " + str(type(course))
    print "  has " + str(course.calories) + " calories " 
    print "  and tastes like " + course.tastesLike()
                                                                                                  
