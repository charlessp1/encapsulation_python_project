class Fan:

    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__ (self, speed, power_on=False, radius, color, ):
        self.__speed = speed
        self.__power_on = power_on
        self.__radius = float(radius)
        self.__color = color
        