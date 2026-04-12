# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_plant_types.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: maratojo <maratojo@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/12 15:06:00 by maratojo        #+#    #+#               #
#  Updated: 2026/04/12 17:16:30 by maratojo        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
class Flower(Plant):
    def __init__(self, name :str, height: float, age: int):
        super().__init__(name, height, age)

