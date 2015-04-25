'''
@summary: Python Intro - Classes
'''
# ---------------------------
# class 
# ---------------------------

class Vehicle(object):

    def __init__(self, name):
        """ Constructor """
        self.name = name
   
    def __str__(self, *args, **kwargs):
        return "Vehicle class" + self.name
        # return object.__str__(self, *args, **kwargs)

    def __del__(self):
        """
        destructor - is called when class is garbage collected
        :return:
        """
        pass

    def move(self, distance=1):
        raise NotImplementedError()
    
    def capabilities(self):
        """
        :return: list of capabilities
        """
        return ["moveable", ]

# ---------------------------
# inheritance
# ---------------------------

class Car(Vehicle):

    def __init__(self, make, name):
        # Call base class constructor
        Vehicle.__init__(self, name)
        self.make = make
    
    def move(self, distance=1):  # overriding base class method
        """
        :param distance: int how far does the car move?
        :return:
        """
        print "%s-%s moved %d feet" % (self.make, self.name, distance)
 
    def capabilities(self):
        parent_capabilities = Vehicle.capabilities(self)  # super method call
        my_capabilities = ["fuel-using", "transporter"]
        return parent_capabilities + my_capabilities

        
# ---------------------------
# Instantiate no new needed
# ---------------------------
car = Car("Mercedes", "SL500")
print car

# ---------------------------
# access methods with . notation
# ---------------------------
car.move(34)
print car.capabilities()

# ---------------------------
# access properties with . notation
# ---------------------------
print car.name
