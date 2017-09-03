class Car():
    # A set of classes used to represent gas and electric cars.

    def __init__(self, make, model, year):
        # Initialize variables to describe a car.
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        # Return a neatly formatted descriptive name.
        long_name = "{} {} {}".format(self.year, self.make, self.model)
        return long_name.title()

    def read_odometer(self):
        # Print a statement showing the car's mileage.
        print("The car has {} miles on it.".format(self.odometer_reading))

    def update_odometer(self, mileage):
        '''
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        '''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        # Add the given amount to the odometer reading.
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print("The gas tank was filled!")
        

class Battery():
    # Modeling a car's battery.

    def __init__(self, battery_size=70):
        # Initialize the battery's attributes.
        self.battery_size = battery_size

    def describe_battery(self):
        # Print a statement describing the battery size.
        print("This car has a {}-kWh battery.".format(self.battery_size))

    def get_range(self):
        # Print a statement about the range this battery provides.
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately {} miles on a full charge.".format(range)
        print(message)


class ElectricCar(Car):
    # Represents aspects of a car, specific to electric vehicles.
    def __init__(self, make, model, year):
        # Initialize attributes of parent class.
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        # Print a statement describing the battery size.
        print("This car has a {}-kWh battery.".format(self.battery_size))

    def fill_gas_tank(self):
        # Electric cars don't have gas tanks.
        print("This car doesn't need a gas tank!")
'''
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(50)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
'''
