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
    name: str
    height: int
    age: int

    def growth(self):
        self.height = round(self.height + 0.8, 1)

    def gr_age(self):
        self.age += 1


if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25
    rose.age = 30
    init_height = rose.height
    print("=== Garden Plant Growth ===")
    for i in range(1, 8):
        print("=== Day {} ===".format(i))
        print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
        rose.growth()
        rose.gr_age()
        i += 1
    print("Growth this week:", (round(rose.height - init_height)), "cm")
