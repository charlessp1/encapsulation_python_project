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
        pass

    def get_power_on(self):
        pass

    def get_radius(self):
        pass

    def get_color(self):
        pass

    def set_speed(self):
        pass

    def set_power_on(self):
        pass

    def set_radius(self):
        pass

    def set_color(self):
        pass

