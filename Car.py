class Car:
    def __init__(self, id=None, make=None, model=None, color=None, year=None):
        self.id = id
        self.make = make
        self.model = model
        self.color = color
        self.year = year

    # Return car object as string value
    def __str__(self):
        return f'{self.make} {self.model} {self.color} {self.year}'

    # Get methods for attributes
    def getID(self):
        return self.id

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getColor(self):
        return self.color

    def getYear(self):
        return self.year

    # Set methods for attributes
    def setID(self, id):
        self.id = id

    def setMake(self, make):
        self.make = make

    def setModel(self, model):
        self.model = model

    def setColor(self, color):
        self.color = color

    def setYear(self, year):
        self.year = year
