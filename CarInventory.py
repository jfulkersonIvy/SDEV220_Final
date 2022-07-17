class CarInventory:
    def __init__(self, carList=None):
        self.carList = carList

    # Get method for attribute
    def getCarList(self):
        return self.carList

    # set method for attribute
    def setCarList(self, carList):
        self.carList = carList

    # Add to the car list inventory as a dictionary structure
    def addCar(self, car, index):
        self.carList.insert(index,{'id': car.getID(), 'make': car.getMake(), 'model': car.getModel(), 'color': car.getColor(), 'year': car.getYear()})
        return (" Added: " + str(car) + ".")

    # Remove from car list inventory as a dictionary structure
    def removeCar(self, car):
        removed = 0
        carDict = {'id': car.getID(), 'make': car.getMake(), 'model': car.getModel(), 'color': car.getColor(),'year': car.getYear()}
        for x in self.carList:
            if carDict['make'] == x['make'] and carDict['model'] == x['model'] and carDict['color'] == x['color'] and carDict['year'] == x['year']:
                self.carList.remove(x)
                removed += 1
                return (" Removed: " + str(car) + ".")
            elif carDict['id']!="" and int(carDict['id']) == int(x['id']):
                self.carList.remove(x)
                removed += 1
                return (" Removed: " + x['make'] + " " + x['model'] + " " + x['color'] + " " + x['year'] + ".")

        if removed == 0:
            return " No car found."