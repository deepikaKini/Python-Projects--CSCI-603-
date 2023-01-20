__author__ = 'dk1346'

"""
CSCI-603: Lab 6 (stacks and queues) 
Author: Deepika Kini

the bunker file helps create data structure to store soldiers
 and provides details to Rescue_mission file
"""
from player import Player, Role
from cs_queue import Queue


class Bunker:
    __slots__ = "bunker_queue", "_num_soldiers"

    def __init__(self, num_soldiers):
        """"
        Create the bunker and populate it with the given number of soldiers.
        Each soldier will be created with an id ranging between 1 and num_soldiers.
        @param num_soldiers: the total number of soldiers that start in the bunker
        """
        # stores a queue that loads soldier type Players
        self.bunker_queue = Queue()
        self._num_soldiers = num_soldiers
        for i in range(1, num_soldiers + 1):
            self.bunker_queue.enqueue(Player(i, Role.SOLDIER))

    def deploy_next_soldier(self) -> Player:
        """
        Remove the next soldier from the front of the bunker to be deployed
        on a rescue attempt.
        :pre: The bunker is not empty
        :return: the soldier at the front of the bunker
        """
        # remove next soldier from the bunker. Checks if bunker is not empty first
        if self.bunker_queue.is_empty():
            print("bunker is empty")
        else:
            self._num_soldiers = self._num_soldiers - 1
            soldier = self.bunker_queue.peek()
            self.bunker_queue.dequeue()
            return soldier

    def fortify_soldier(self, soldier: Player) -> None:
        """"Add the soldier at the end of the bunker
        :param: the soldier to add
        :return: None"""
        self.bunker_queue.enqueue(soldier)
        self._num_soldiers = self._num_soldiers + 1

    def get_num_soldiers(self) -> int:
        """
        Get how many soldiers are in the bunker.
        :return: The number of soldiers in the bunker.
        """
        return self._num_soldiers

    def has_soldiers(self) -> bool:
        """
        Are soldiers left in the bunker?
        :return: whether the bunker has soldiers or not
        """
        return self._num_soldiers != 0
