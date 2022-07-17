import Search, Car, Customer, Storage, CarInventory


if __name__ == '__main__':
    # Create Inventory From JSON Data
    storage = Storage.Storage()
    carInventory = CarInventory.CarInventory(storage.read()[0])


    # Create Car Object
    myCar1 = Car.Car(7, 'dodge', 'ram', 'red', 2018)

    # Methods to Add Car to Inventory
    carInventory.addCar(myCar1)
    carInventory.removeCar(myCar1)

    # Search on Inventory Object
    search = Search.Search()
    search.search(carInventory.getCarList())

    # Write Updated Inventory to JSON file
    storage.write(carInventory.getCarList())
