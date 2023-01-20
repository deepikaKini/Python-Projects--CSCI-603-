__author__ = 'dk1346'

"""
CSCI-603: Lab 6 (stacks and queues) 
Author: Deepika Kini

the bunker file helps create data structures to store hostages
and guerrillas and provides details to Rescue_mission file
"""
import random

from cs_stack import Stack
from cs_queue import Queue
from player import Player, Role


class Enemy_Base:
    __slots__ = "_num_hostages", "_num_guerrillas", "rnd", "hostage_stack", "guerrillas_queue"

    def __init__(self, num_hostages, num_guerrillas, rnd):
        self.hostage_stack = Stack()
        self.guerrillas_queue = Queue()
        self._num_hostages = num_hostages
        self._num_guerrillas = num_guerrillas
        self.rnd = rnd#not required
        # initialising the hostage stack with hostages
        for i in range(num_hostages):
            self.hostage_stack.push(Player(i + 1, Role.HOSTAGE))
        # initialising the guerrilla queue with guerrillas
        for i in range(num_guerrillas):
            self.guerrillas_queue.enqueue(Player(i + 1, Role.GUERRILLA))

    def add_guerrilla(self, guerrilla):
        self.guerrillas_queue.enqueue(guerrilla)
        self._num_guerrillas += 1

    def add_hostage(self, hostage):
        self.hostage_stack.push(hostage)
        self._num_hostages += 1

    def get_guerrillas(self):
        self._num_guerrillas -= 1
        guerrilla = self.guerrillas_queue.peek()
        self.guerrillas_queue.dequeue()
        return guerrilla

    def get_hostage(self):
        self._num_hostages = self._num_hostages - 1
        hostage = self.hostage_stack.peek()
        self.hostage_stack.pop()
        return hostage

    def get_num_guerrillas(self):
        return self._num_guerrillas

    def get_num_hostages(self):
        return self._num_hostages

    def rescue_hostage(self, soldier: Player):
        print(soldier, "enters enemy base...")
        # random.seed(self.rnd) - not required to be called
        hostage = self.get_hostage()
        if self.get_num_guerrillas() == 0:
            return hostage
        # else:
        guerrilla: Player = self.get_guerrillas()
        rand_int = random.randint(1, 100)
        print(str(soldier), "battles", str(guerrilla), "who rolls a", rand_int)
        if rand_int > Player.GUERRILLA_CHANCE_TO_BEAT_SOLDIER:
            soldier.print_victory_message(guerrilla)
            return hostage
        else:
            guerrilla.print_victory_message(soldier)
            self.add_hostage(hostage)
            self.add_guerrilla(guerrilla)
            return None
