#!/usr/bin/env python3
# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: maratojo <maratojo@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/12 15:06:00 by maratojo        #+#    #+#               #
#  Updated: 2026/05/05 08:59:37 by maratojo        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0.0
        self._age = 0
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = round(height, 1)
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age = age

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> float:
        return (self._age)

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
        else:
            self._height = round(height + 0.0, 1)

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
        else:
            self._age = age


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str):
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float):
        super().__init__(name, height, age)
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of {self._height}cm"
              f" long and {self._trunk_diameter}cm wide.")

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int, harvest_season: str):
        super().__init__(name, height, age)
        self._nutritional_value = 0.0
        self._harvest_season = harvest_season

    def age(self) -> None:
        self._age += 1
        self._nutritional_value += 0.5

    def grow(self) -> None:
        self._height = round(self._height + 2.1, 1)
        self._nutritional_value += 0.5

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {round(self._nutritional_value)}")

    def grow_and_age(self, value: int) -> None:
        for i in range(value):
            self.grow()
            self.age()


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.grow_and_age(20)
    tomato.show()
