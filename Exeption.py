# This is a example of exception class
# The lover's coffee recommend drink coffee   when it there between in 50°C and 60°C. This script to help you find this
# ideal temperature, you input its coffee temperature and it will return the warnings.


class CoffeeCup(Exception):
    """"Clase base de excepciones"""


class CoffeeTooHot(CoffeeCup):
    """raised when the coffee is too hot"""

    def __init__(self, temperature, message="Coffee is too hot"):
        self.temperature = temperature
        self.message = message
        super().__init__(self.message)


class CoffeeTooCold(CoffeeCup):
    """raised when the coffee is too Cold"""

    def __init__(self, temperature, message="Coffee is too cold"):
        self.temperature = temperature
        self.message = message
        super().__init__(self.message)


while True:
    try:
        temp = int(input("Enter temperature of coffee (in celsius degree): "))
        if temp > 60:
            raise CoffeeTooHot(temp)
        elif temp < 50:
            raise CoffeeTooCold(temp)
        break
    except CoffeeTooHot:
        print("The coffee is too hot, wait a moment, the ideal range is (50,60)")
        print()
    except CoffeeTooCold:
        print("The coffee is too cold, reheat the coffee")
        print()

print("The temperature is perfect, it's time to enjoy <3.")

# Examples:
# >>>  Enter temperature of coffee (in celsius degree): 20
# >>>  The coffee is too cold, reheat the coffee
# >>>  Enter temperature of coffee (in celsius degree): 80
# >>>  The coffee is too hot, wait a moment, the ideal range is (50,60)
# >>>  Enter temperature of coffee (in celsius degree): 55
# >>>  The temperature is perfect, it's time to enjoy <3.
