# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_data.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: maratojo <maratojo@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/25 19:51:58 by maratojo        #+#    #+#               #
#  Updated: 2026/04/27 14:43:35 by maratojo        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

class Plant:
    name: str
    height: int
    age: int
SHOW

if __name__ == "__main__":
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25
    rose.age = 30

    sunflower = Plant()
    sunflower.name = "Sunflower"
    sunflower.height = 80
    sunflower.age = 45

    cactus = Plant()
    cactus.name = "Cactus"
    cactus.height = 15
    cactus.age = 120

    plants = [rose, sunflower, cactus]
    for i in range(len(plants)):
        plant = plants[i]
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
