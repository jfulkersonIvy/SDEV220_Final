"""
Current working gui

 - Need input validation
"""
import tkinter
import tkinter.messagebox
import customtkinter, Storage, CarInventory, Car, Search


# customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    WIDTH = 1080
    HEIGHT = 720
    TEXT = ("Roboto Medium", -16)

    def __init__(self):
        super().__init__()
        # Load Data and Create Objects
        self.storage = Storage.Storage()
        self.carInventory = CarInventory.CarInventory(self.storage.read()[0])

        self.title("Car Application")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============
        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(6, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.navigator = customtkinter.CTkLabel(master=self.frame_left, text="Car Inventory", text_font=App.TEXT)
        self.navigator.grid(row=1, column=0, pady=10, padx=10)

        self.home_button = customtkinter.CTkButton(master=self.frame_left, text="Catalog", text_font=App.TEXT, command=self.Catalog)
        self.home_button.grid(row=2, column=0, pady=10, padx=20)

        self.add_car_button = customtkinter.CTkButton(master=self.frame_left, text="Update Cars", text_font=App.TEXT,command=self.UpdateCar)
        self.add_car_button.grid(row=3, column=0, pady=10, padx=20)


        self.color_mode_title = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:",
                                                       text_font=App.TEXT)
        self.color_mode_title.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.color_mode_toggle = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                             values=["Light", "Dark", "System"],
                                                             text_font=App.TEXT,
                                                             command=self.change_appearance_mode)
        self.color_mode_toggle.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============
        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=10)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=0)

        # ============ frame_right ============
        # set default values
        self.color_mode_toggle.set("Dark")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # When app is closed, write any updates to the car list
    def on_closing(self, event=0):
        self.storage.write(self.carInventory.getCarList())
        self.destroy()

    # Create a popup and move to top level view - used to give confirmation during events
    def open_popup(self, text):
        top = customtkinter.CTkToplevel()
        top.geometry("300x50")
        top.title("Verification")
        customtkinter.CTkLabel(top, text=text).grid(row=0, column=0)


    # Used to save the next created car in the right ID position within the list
    # This will search the current car list to find open ID positions and return the first ID available
    # Example: if current list IDs are 1, 2, 4, 5, 6 - This will find 3 and save the next added car as ID 3
    def getNextID(self):
        for x in range(0,len(self.carInventory.getCarList())):
            # If an open position is found, we return the open position
            if (x < len(self.carInventory.getCarList()) - 1 and self.carInventory.getCarList()[x]['id'] != self.carInventory.getCarList()[x + 1]['id'] - 1):
                return self.carInventory.getCarList()[x]['id'] + 1
        # If no open position is found within the current list, next ID is returned as the length + 1
        return len(self.carInventory.getCarList()) + 1

    def UpdateCar(self):
        # Creates Update Car tab view

        # Add car to inventory
        def addCar():
            # Use getNextID to find open positions in list so cars remain in order of ID
            car = Car.Car(self.getNextID(), add_items[1][0].get(), add_items[1][1].get(), add_items[1][2].get(), add_items[1][3].get())
            add_items[1][0].delete(0, customtkinter.END)
            add_items[1][1].delete(0, customtkinter.END)
            add_items[1][2].delete(0, customtkinter.END)
            add_items[1][3].delete(0, customtkinter.END)
            # If user tries to add a car with missing values, an error is displayed
            if(car.getMake=="" or car.getModel()=="" or car.getColor()=="" or car.getYear()==""):
                self.open_popup(" Insufficient information provided. ")
                return
            # Add car in next available ID position
            # Subtract 1 due to dictionary position starting at zero
            else:
                self.open_popup(self.carInventory.addCar(car,car.getID()-1))

        # Remove car from inventory
        def removeCar():
            car = Car.Car(remove_items[1][0].get(), remove_items[1][1].get(), remove_items[1][2].get(), remove_items[1][3].get(), remove_items[1][4].get())
            remove_items[1][0].delete(0, customtkinter.END)
            remove_items[1][1].delete(0, customtkinter.END)
            remove_items[1][2].delete(0, customtkinter.END)
            remove_items[1][3].delete(0, customtkinter.END)
            remove_items[1][4].delete(0, customtkinter.END)
            # Confirmation message when car is removed
            self.open_popup(self.carInventory.removeCar(car))


        add_items = [[], []]
        remove_items = [[], []]
        items = ('ID','Make', 'Model', 'Color', 'Year')

        self.updateCarFrame = customtkinter.CTkFrame(master=self)  # Embedded Frame == (master=self.frame_right) and column=0
        self.updateCarFrame.grid(row=0, column=1, sticky="nswe", padx=30, pady=30)  # Full Frame == (master=self) and column=1

        for element in range(4):
            add_items[0].append(
                customtkinter.CTkLabel(master=self.updateCarFrame, text=f'{items[element+1]}:', text_font=App.TEXT))
            add_items[0][element].grid(row=element, column=0, padx=0, pady=15)

            add_items[1].append(customtkinter.CTkEntry(master=self.updateCarFrame, text_font=App.TEXT))
            add_items[1][element].grid(row=element, column=1, sticky="w", columnspan=2)

        for element in range(5):
            if element == 1:
                r = element + 1
                orLabel = customtkinter.CTkLabel(master=self.updateCarFrame, text='OR', text_font=App.TEXT)
                orLabel.grid(row=element, column=4, padx=0, pady=0)
            elif element > 0:
                r = element+1
            else:
                r = element

            remove_items[0].append(
                customtkinter.CTkLabel(master=self.updateCarFrame, text=f'{items[element]}:', text_font=App.TEXT))
            remove_items[0][element].grid(row=r, column=3, padx=0, pady=15)

            remove_items[1].append(customtkinter.CTkEntry(master=self.updateCarFrame, text_font=App.TEXT))
            remove_items[1][element].grid(row=r, column=4, sticky="w", columnspan=2)

        self.add_car_button = customtkinter.CTkButton(master=self.updateCarFrame, text="Add Car", command=addCar)
        self.remove_car_button1 = customtkinter.CTkButton(master=self.updateCarFrame, text="Remove Car",command=removeCar)
        self.add_car_button.grid(row=4, column=1)
        self.remove_car_button1.grid(row=6, column=4)

    def Catalog(self):
        # Create Catalog tab view

        # Allow searches based on results from all categories
        def searchCar():
            search = Search.Search()
            searchResults = search.search(self.searchEntry.get(),self.carInventory.getCarList())
            # If nothing is searched, the entire catalog will be displayed
            if len(searchResults)==0:
                searchResults = self.carInventory.getCarList()
            
            # Create a separate label for each car so they are all displayed upon starting application
            for x in range(0,100):
                if(x>=len(searchResults)):
                    newText = ""
                else:
                    newText = searchResults[x]['make']+" "+searchResults[x]['model']+" "+searchResults[x]['color']+" "+str(searchResults[x]['year'])
                label = self.carTable[x]
                label.configure(text=newText)

        self.searchFrame = customtkinter.CTkFrame(master=self)  # Embedded Frame == (master=self.frame_right) and column=0
        self.searchFrame.grid(row=0, column=1, sticky="nswe", padx=30, pady=30)  # Full Frame == (master=self) and column=1

        self.searchLabel = customtkinter.CTkLabel(master=self.searchFrame, text="Keywords: ", text_font=App.TEXT)
        self.searchLabel.grid(row=0, column=0, padx=0, pady=15)

        self.searchEntry = customtkinter.CTkEntry(master=self.searchFrame, text_font=App.TEXT)
        self.searchEntry.grid(row=0, column=1, sticky="w", columnspan=2)

        self.searchButton = customtkinter.CTkButton(master=self.searchFrame, text="Search", command=searchCar)
        self.searchButton.grid(row=0, column=2, padx=0, pady=15)

        self.carTable = []
        self.cars = self.carInventory.getCarList()
        for x in range(0,100):
            if(x>=len(self.cars)):
                text = ""
            else:
                text = self.cars[x]['make']+" "+self.cars[x]['model']+" "+self.cars[x]['color']+" "+str(self.cars[x]['year'])

            self.carTable.append(customtkinter.CTkLabel(master=self.searchFrame, text=text))
            self.carTable[x].grid(row=x+1, column=1, padx=0, pady=15)


if __name__ == "__main__":
    app = App()
    app.mainloop()
