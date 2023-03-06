class Car:

    wheels=4        #class variable
    #a class variable is a variable inside the class but outside the constructor
    #__init__ is a constructor in python
    def __init__(self,make,model,year,colour):        #while calliong a function dont need to pass self but while defining function it is necessary
        #instance variable is a variable which is inside the constructor
        self.make=make               #instance variable                          
        self.model=model             #instance variable 
        self.year=year              #instance variable
        self.colour=colour           #instance variable
        
    def drive(self):
        print("the " +self.model +" is driving")    #in simple words self acts as a link between object in real function and its class which is created at different place
    def stop(self):
        print("car is stopped")