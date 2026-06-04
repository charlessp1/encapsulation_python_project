from main import Fan

FAST = Fan.FAST
MEDIUM = Fan.MEDIUM
SLOW = Fan.SLOW
first_fan = Fan()
second_fan = Fan()

class TestFan:
    def enter_values(self):
        first_fan.set_speed(FAST)
        first_fan.set_power_on(True)
        first_fan.set_radius(10)
        first_fan.set_color("yellow")

        second_fan.set_speed(MEDIUM)
        second_fan.set_power_on(False)
        second_fan.set_radius(5)
        second_fan.set_color("blue")

        print("Values assigned to First Fan and Second Fan successfully!")
        print("Do you want to display each object's speed, power, radius, and color? [Y/N]:")
        choice = input("> ")

        while True:
            if choice.upper() == 'Y':
                self.show_values()
            elif choice.upper() == 'N':
                break
            else:
                print("Invalid input! Please try again.")

    def show_values(self):
        first_fan.get_speed()
        first_fan.get_power_on()
        first_fan.get_radius()
        first_fan.get_color()

        second_fan.get_speed()
        second_fan.get_power_on()
        second_fan.get_radius()
        second_fan.get_color()

run_test = TestFan()
run_test.enter_values()