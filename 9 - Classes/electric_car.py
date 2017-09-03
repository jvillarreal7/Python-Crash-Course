from car import Car
from battery import Battery

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


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
# my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
