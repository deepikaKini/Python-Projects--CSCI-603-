__author__ = 'dk1346'

"""
CSCI-603: Lab 6 (stacks and queues) 
Author: Deepika Kini

this is the file that creates the chopper object and pushes and pops to recue
passengers(soldiers and hostages)

"""

from cs_stack import Stack
class Chopper:
    __slots__ = "chopper" , "_occupancy", "_num_rescued"

    MAX_OCCUPANCY = 6

    def __init__(self):
        self.chopper = Stack()
        self._occupancy = 0
        self._num_rescued = 0


    def board_passenger(self, passenger):
        """
        boards passengers in the chopper isn't filled
        else rescues , then inserts passengers
        :param passenger: the hostage or soldier object
        :return: None
        """
        if self._occupancy < Chopper.MAX_OCCUPANCY:
            self.chopper.push(passenger)
            self._occupancy += 1
            print(str(passenger) , "boards the chopper!")
            if self._occupancy == Chopper.MAX_OCCUPANCY:
                self.rescue_passengers()
            # print(self.chopper)
            # print("occupancy :" , self.occupancy)
        else:
            self.rescue_passengers()
            self.chopper.push(passenger)
            print(passenger, "boards the chopper!")
            self._occupancy += 1

    def get_num_rescued(self):
        return self._num_rescued

    def is_empty(self):
        return self.chopper.is_empty()

    def is_full(self):
        return (self._occupancy == Chopper.MAX_OCCUPANCY)


    def rescue_passengers(self):
        """"
        When the chopper is full, or it is the last group of people to be rescued,
        it will fly away and rescue the passengers.(logic in   Each passenger exits the
        chopper in the reverse order they entered it, e.g. the last passenger to
        enter exits first.
        """
        occupied = self._occupancy
        for i in range(occupied):
            print("Chopper transported", self.chopper.peek(), "to safety!")
            self._num_rescued += 1
            self.chopper.pop()
            self._occupancy -= 1
        # print(self.num_rescued)


    def get_occupancy_of_chopper(self):
        return self._occupancy
