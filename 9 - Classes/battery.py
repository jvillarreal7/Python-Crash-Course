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
