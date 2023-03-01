class Car:
    #__init__ is a constructor in python
    def __init__(self,make,model,year,colour):        #while calliong a function dont need to pass self but while defining function it is necessary
        self.make=make                               
        self.model=model
        self.year=year
        self.colour=colour
        
    def drive(self):
        print("the " +self.model +" is driving")    #in simple words self acts as a link between object in real function and its class which is created at different place
    def stop(self):
        print("car is stopped")