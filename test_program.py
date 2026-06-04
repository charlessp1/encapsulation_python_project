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

        while True:
            choice = input("> ")
            if choice.upper() == 'Y':
                self.show_values()
                break
            elif choice.upper() == 'N':
                break
            else:
                print("Invalid input! Please try again.")

    def show_values(self):
        print(f"Fan 1 Speed: {first_fan.get_speed()}")
        print(f"Fan 1 Power: {first_fan.get_power_on()}")
        print(f"Fan 1 Radius: {first_fan.get_radius()}")
        print(f"Fan 1 Color:{first_fan.get_color()}\n")

        print(f"Fan 2 Speed: {second_fan.get_speed()}")
        print(f"Fan 2 Power: {second_fan.get_power_on()}")
        print(f"Fan 2 Radius: {second_fan.get_radius()}")
        print(f"Fan 2 Color: {second_fan.get_color()}")

run_test = TestFan()
run_test.enter_values()