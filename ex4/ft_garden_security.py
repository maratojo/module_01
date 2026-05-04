# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_security.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: maratojo <maratojo@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/25 20:12:32 by maratojo        #+#    #+#               #
#  Updated: 2026/04/27 09:51:29 by maratojo        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name: str, height: float, age: int):
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

    def get_height(self) -> float:
        return (self._height)

    def get_age(self) -> float:
        return (self._age)

    def set_height(self, height: int) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = round(height + 0.0, 1)
            print(f"Height updated: {height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days")

    def show(self) -> None:
        print(f"Plant created: {self._name}: "
              f"{self._height}cm, {self._age} days old")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    rose.show()
    rose.set_height(-25)
    rose.set_height(20)
    rose.set_age(32)
    rose.set_age(-30)
    print(
        f"Current state: {rose._name}: {rose.get_height()}cm, "
        f"{rose.get_age()} days old")
