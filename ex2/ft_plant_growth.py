#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_growth.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: maratojo <maratojo@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/25 19:33:43 by maratojo            #+#    #+#            #
#   Updated: 2026/03/25 19:56:44 by maratojo           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name.capitalize()
        self.height = height
        self.ag = age

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age(self) -> None:
        self.ag += 1

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.ag} days old")


if __name__ == "__main__":
    rose = Plant("Rose", 25.0, 30)
    init_height = rose.height
    print("=== Garden Plant Growth ===")
    rose.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        rose.show()
    print(f"Growth this week: {round((rose.height - init_height), 1)}cm")
