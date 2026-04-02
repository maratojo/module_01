# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_security.py                             :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: maratojo <maratojo@student.42antananari   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/25 20:12:32 by maratojo        #+#    #+#               #
#  Updated: 2026/03/25 20:12:39 by maratojo        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self._height = height
        self._age = age
        print(f"Plant created: {self.name}: {self._height}cm, {self._age} days old")
    def get_height(self) -> float:
        return (self._height)
    def get_age(self) -> float:
        return (self._age)
    def set_height(self, height) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't negative")
            print(f"Height update rejected")
        else:
            self._height = height
            print(f"Height updated: {height}cm")
    def set_age(self, age) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't negative")
            print(f"Age update rejected")
        else:
            self._age = age
            print(f"Age updated: {age} days")

if __name__ == "__main__":
    print (f"=== Garden Security System ===")
    rose = Plant("Rose", 15, 10)
    rose.set_height(25)
    rose.set_age(30)
    rounds = round(rose.get_height(), 1)
    print(f"Current state: {rose.name}: {rounds}cm, {rose.get_age()} days old")
