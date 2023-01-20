__author__ = 'dk1346'

"""
CSCI-603: Lab 6 (stacks and queues) 
Author: Deepika Kini

the file creates Player objects using enums for role names
"""

from enum import Enum

class Role(Enum):
    """
    An enum to represent the possible roles of a player
    """
    GUERRILLA = 4
    HOSTAGE = 3
    PREDATOR = 2
    SOLDIER = 1

    def __members__(self):
        for iterator_enum in Role:
            print(iterator_enum.name, iterator_enum.value)

class Player:
    """
    A class to represent a player. Every player has:
    - an id
    - a role: Predator, Soldier, Hostage or Guerrilla

    Every player has a unique combination of id and role.
    """
    __slots__ = "id", "role"
    role: Role
    id: int

    # as per pdf(not html)
    GUERRILLA_CHANCE_TO_BEAT_SOLDIER = 20
    PREDATOR_CHANCE_TO_BEAT_HOSTAGE = 50
    PREDATOR_CHANCE_TO_BEAT_SOLDIER = 75



    def __init__(self, id, role):
        """
        Create a new player.
        @param id: the id of the player
        @param role: the role of the player
        :param id: id of player
        :param role: role of player
        """
        self.role = role
        self.id = id

    def __str__(self):
        """
        The string representation of a player is:
        "{role} #{id}"
        @return: the player string
        :return: None
        """
        #using name data descriptor to access "key" of enum
        return str(self.role.name) + " #" + str(self.id)

    def print_victory_message(self, opponent):
        """
        If the player is triumphant over the opponent, it displays the message:
        "{player} defeats {opponent}"
        @param opponent: the defeated player
        @return: None
        :param opponent:the defeated player
        :return: None
        """
        print(str(self), "defeats", str(opponent))

