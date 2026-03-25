# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ft_garden_intro.py                                :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: maratojo <maratojo@student.42antananari   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/25 19:51:20 by maratojo        #+#    #+#               #
#  Updated: 2026/03/25 19:51:28 by maratojo        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #


def ft_garden_intro(name: str, heigh: int, age: str):
    print("Plant:", name)
    print(f"Height: {heigh}cm")
    print("Age:", age)


if __name__ == "__main__":
    ft_garden_intro("Rose", 25, "30 days")
