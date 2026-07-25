from random import randint, choice
import time

targets = ("infantry", "building", "bunker", "trench", "light armored unit", "heavy armored unit", "minefield")
directions = ("N", "S", "W", "E")


class EnemyInfo:

    @staticmethod
    def set_distance():
        meters = randint(100, 1000)
        centimeters = randint(1, 100)
        distance = meters + centimeters/100
        print(f"Target is {round(distance)} meters from you!")

    @staticmethod
    def set_direction():
        direction = choice(directions)
        degree = randint(0, 360)
        print(f"Direction: {direction}{degree}")

    @staticmethod
    def set_time_limit():
        seconds_limit = randint(60, 300)
        minutes = (seconds_limit % 3600) // 60
        print(f"You have only {minutes} minute(s) to shot!")

    @staticmethod
    def set_target():
        target = choice(targets)
        print(f"Target: {target}")

    @staticmethod
    def set_wind():
        speed = randint(0, 12)
        direction = choice(directions + ("NE", "NW", "SE", "SW"))
        print(f"Wind {speed} km/h, direction: {direction}" if speed > 0 else f"Wind {speed} km/h\n")

    @staticmethod
    def get_direction_help():
        print("\n"
              "N - 0°, NE - 45°, E - 90°, SE - 135, S - 180°, SW - 225°, W - 270°, NW - 315°\n"
              "Direction + degree = desired degree\n"
              "If desired degree > 360°: desired degree - 360°\n")

    def __call__(self):
        self.get_direction_help()
        self.set_distance()
        self.set_direction()
        self.set_wind()
        self.set_target()
        self.set_time_limit()


class Ammunition:
    def __init__(self, name, targets_, distance_range, degree_range, kill_radius, damage_radius):
        self.name = name
        self.targets = targets_
        self.distance_range = distance_range
        self.degree_range = degree_range
        self.kill_radius = kill_radius
        self.damage_radius = damage_radius

    def __str__(self):
        return (f"Type: {self.name}\n"
              f"Targets: {self.targets}\n"
              f"Distance: {self.distance_range[0]}-{self.distance_range[-1]}m\n"
              f"Degree: {self.degree_range[0]}°-{self.degree_range[-1]}°\n"
              f"Kill radius: {self.kill_radius[0]}-{self.kill_radius[-1]}\n"
              f"Damage radius: {self.damage_radius[0]}-{self.kill_radius[-1]}\n")


high_explosive = Ammunition("high-explosive", ("infantry", "building"), range(30, 61), range(25, 56), range(6, 13), range(15, 26))
anti_tank = Ammunition("anti-tank", ("heavy armored unit", "bunker"), range(10, 801), range(5, 21), range(0, 2), range(1, 4))
cluster = Ammunition("cluster", ("infantry", "light armored unit", "trench", "minefield"), range(80, 451), range(40, 71), range(1, 3), range(3, 6))
cumulative = Ammunition("cumulative", ("heavy armored unit", "bunker"), range(20, 501), range(10, 36), range(0, 2), range(1, 5))
sub_caliber = Ammunition("sub-caliber", ("heavy armored unit", "bunker"), range(5, 1201), range(2, 11), range(0, 2), range(0, 2))
ammunition_list = [high_explosive, anti_tank, cluster, cumulative, sub_caliber]


class ArtilleryInfo:
    direction_range = range(0, 361)
    degree_range = range(0, 86)

    def __init__(self):
        self.x_degree = self.y_degree = 0
        self.ammunition_type = cumulative

    def get_current_info(self):
        print(f"Direction: N{self.x_degree}")
        print(f"Angle: {self.y_degree}°")

    @staticmethod
    def get_degree_help():
        print("angle = min angle + (max angle - min angle) * (distance / max range)\n")

    def set_x(self):
        while True:
            print("\nSet direction: (0, 360)")
            try:
                self.x_degree = int(input("X: "))
                if self.x_degree not in self.direction_range:
                    print("Wrong degree!")
                else:
                    break
            except Exception:
                print("Wrong degree!")

    def set_y(self):
        self.get_degree_help()
        while True:
            print("Set degree: (0, 90)")
            try:
                self.y_degree = int(input("Y: "))
                if self.y_degree not in self.degree_range:
                    print("Wrong degree!")
                else:
                    break
            except Exception:
                print("Wrong degree!")

    def set_ammunition_type(self):
        print("Set ammunition type:")
        for indx, amm in enumerate(ammunition_list, 1):
            print(f"{indx}. {amm.name}: {str(amm)}")
        while True:
            amm_type = input("<<< ")
            if amm_type not in ammunition_list:
                print("Wrong ammunition type!")
            else:
                self.ammunition_type = ammunition_list[[ammunition.name for ammunition in ammunition_list].index(amm_type)]
                break

    @staticmethod
    def shot():
        code = randint(111, 999)
        print(f"Code: {code}")
        while True:
            try:
                answer = int(input("Repeat code: "))
                if answer != code:
                    print("Wrong code!")
                else:
                    input("Press ENTER to shot!")
                    break
            except Exception:
                print("Wrong code!")

    def validate_shot(self):
        time.sleep(randint(3, 10))
        position = self.ammunition_type.distance_range[0] + (self.ammunition_type.distance_range[-1]-self.ammuni

    def __call__(self):
        enemy = EnemyInfo()
        enemy()
        self.get_current_info()
        self.set_x()
        #self.set_ammunition_type()
        self.set_y()
        self.shot()
        self.validate_shot()


artillery = ArtilleryInfo()
artillery()
