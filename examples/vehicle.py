#!/usr/bin/env python



class Vehicle(object):
    vehiclecount = 0
    def __init__(self,vin,year,make,model,color):
        self.vin = vin
        self.year = year
        self.make = make
        self.model = model
        self.color = color

        Vehicle.vehiclecount +=1 
        self.maintenance_history = []

    def getVin(self):
        return self.vin

    def getOptions(self):
        raise AttributeError




class Car(Vehicle):
    def __init__(self,vin,year,make,model,color,caroptions):
        self.caroptions = caroptions
        super(Car,self). __init__(vin,year,make,model,color)

    def getOptions(self):
        return(self.caroptions)
        
class Truck(Vehicle):
    def __init__(self,vin,year,make,model,color,truckoptions):
        self.truckoptions = truckoptions
        super(Truck,self). __init__(vin,year,make,model,color)
    
    def getOptions(self):
        return(self.truckoptions)




vehiclelist=[]


vehiclelist.append(Car(1234,2004,"Toyota","Camry","Silver","Electric Windows"))
vehiclelist.append(Truck(2345,2007,"Mercedes Benz","blah","White","Some option here"))


for vehicle in vehiclelist:
    print vehicle.getVin()
    print vehicle.getOptions()


print "I have ", Vehicle.vehiclecount, " vehicles"




