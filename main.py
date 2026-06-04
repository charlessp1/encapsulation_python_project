class Fan:

    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__ (self, speed=SLOW, power_on=False, radius=5.0, color="blue", ):
        self.__speed = speed
        self.__power_on = power_on
        self.__radius = float(radius)
        self.__color = color

    def get_speed(self):
        return self.__speed

    def get_power_on(self):
        return self.__power_on

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    def set_speed(self, speed):
        self.__speed = speed

    def set_power_on(self, power_on):
        self.__power_on = power_on

    def set_radius(self, radius):
        self.__radius = radius

    def set_color(self, color):
        self.__color = color

