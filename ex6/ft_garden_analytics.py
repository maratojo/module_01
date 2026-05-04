# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_analytics.py                            :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: maratojo <maratojo@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/27 09:22:10 by maratojo        #+#    #+#               #
#  Updated: 2026/04/27 14:06:51 by maratojo        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    class Stats:
        def __init__(self) -> None:
            self.grow_call = 0
            self.age_call = 0
            self.show_call = 0

        def displays(self) -> None:
            print(
                f"Stats: {self.grow_call} grow, "
                f"{self.age_call} age, "
                f"{self.show_call} show"
            )

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._stats = self.Stats()

    @classmethod
    def creat_anynomuous(cls) -> 'Plant':
        return cls("Unknown plant", 0.0, 0)

    @staticmethod
    def more_than_year(age: int) -> bool:
        return age > 360

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> float:
        return (self._age)

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")
        self._stats.show_call += 1

    def age(self, add_age: int) -> None:
        self._age += add_age
        self._stats.age_call += 1

    def grow(self, value: float) -> None:
        self._height = round(self._height + value, 1)
        self._stats.grow_call += 1


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self.bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self._trunk_diameter = float(trunk_diameter)
        self._shade = 0

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produce a shade of {self._height}cm"
              f" long and {self._trunk_diameter}cm wide.")
        self._shade += 1

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")

    def statistic_tree(self) -> None:
        self._stats.displays()
        print(f" {self._shade} shade ")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seed_count = 0

    def bloom(self) -> None:
        super().bloom()
        self._seed_count = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seed_count}")


def display_stats(plant: Plant) -> None:
    plant._stats.displays()


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    ages = [30, 400]
    for i in range(2):
        print(f"Is {ages[i]} days more than a year? -> "
              f"{Plant.more_than_year(ages[i])}")
    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print(f"[statistics for {rose._name}]")
    display_stats(rose)
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.grow(8.0)
    rose.show()
    print(f"[statistics for {rose._name}]")
    display_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print(f"[statistics for {oak._name}]")
    oak.statistic_tree()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print(f"[statistics for {oak._name}]")
    oak.statistic_tree()

    print("\n=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.bloom()
    sunflower.age(20)
    sunflower.grow(30.0)
    sunflower.show()
    print(f"[statistics for {sunflower._name}]")
    sunflower._stats.displays()
    print("\n=== Anonymous")
    plant = Plant.creat_anynomuous()
    plant.show()
    print("[statistics for Unknown plant]")
    display_stats(plant)
