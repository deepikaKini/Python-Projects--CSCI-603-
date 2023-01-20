__author__ = 'dk1346'

"""
CSCI-603: Lab 6 (stacks and queues) 
Author: Deepika Kini

This is a program runs the rescue mission where soldiers save hostages
from guerrillas and predators

this is the main file that runs all other classes and objects

note:
command prompt entry: python3 rescue_mission.py 0 1000 500 250

"""

import sys
import random
from bunker import Bunker
from enemy_base import Enemy_Base
from player import Player
from chopper import Chopper
from player import Role


class Rescue_Mission:
    __slots__ = "seed", "_bunker", "_enemy_base", "_chopper", "_predator"
    seed: int
    _bunker: Bunker
    _enemy_base: Enemy_Base
    _chopper: Chopper
    _predator: Player

    def __init__(self, seed: int, num_hostages: int, num_soldiers: int, num_guerrillas: int):
        """
        Create the rescue mission. This method is responsible for seeding the random
        number generator and initializing all the supporting classes in the
         simulation: Chopper, Bunker, Enemy_Base and Predator.

        @param seed: the seed for the random number generator
        @param num_hostages: the number of hostages
        @param num_soldiers: the number of soldiers
        @param num_guerrillas: the number of guerrillas

        """
        self.seed = seed
        self._bunker = Bunker(num_soldiers)
        random.seed(self.seed)
        self._enemy_base = Enemy_Base(num_hostages, num_guerrillas, random.seed(self.seed))
        # print(random.seed(self.seed))
        self._chopper = Chopper()
        self._predator = Player(1, Role.PREDATOR)

    def run_simulation(self):
        """
        connects all the logic together and runs the loop until
        there are hostages in the cave.

        :return:None
        """
        print("Get to the choppa!")

        while self._bunker.has_soldiers() == True and self._enemy_base.get_num_hostages() != 0:
            print("Statistics:  " + str(self._enemy_base.get_num_hostages()) +
                  "  hostage/s remain,  " + str(self._bunker.get_num_soldiers())
                  + "  soldier/s remain,  " + str(self._enemy_base.get_num_guerrillas()) +
                  "  guerrilla/s remain,  " + str(self._chopper.get_num_rescued()) + "  rescued")
            soldier = self._bunker.deploy_next_soldier()
            rescued_hostage = self._enemy_base.rescue_hostage(soldier)

            if rescued_hostage is None:
                pass
            else:
                print(rescued_hostage, "rescued from enemy base by", soldier)
                random_int = random.randint(1, 100)
                print(soldier, " encounters the predator who rolls a ", random_int)
                if random_int > Player.PREDATOR_CHANCE_TO_BEAT_SOLDIER:
                    soldier.print_victory_message(self._predator)
                    self._bunker.fortify_soldier(soldier)
                    # hostage board _chopper#
                    self._chopper.board_passenger(rescued_hostage)
                else:
                    self._predator.print_victory_message(soldier)
                    # print(predator, "defeats", soldier)
                    random_int = random.randint(1, 100)
                    print(rescued_hostage, " encounters the predator who rolls a ", random_int)
                    if random_int > Player.PREDATOR_CHANCE_TO_BEAT_HOSTAGE:
                        rescued_hostage.print_victory_message(self._predator)
                        # hostage board _chopper#
                        self._chopper.board_passenger(rescued_hostage)

                        # predator defeats soldier and hostage
                    else:
                        self._predator.print_victory_message(rescued_hostage)

            if self._enemy_base.get_num_hostages() == 0:
                print("Statistics:  " + str(self._enemy_base.get_num_hostages()) +
                      "  hostage/s remain,  " + str(self._bunker.get_num_soldiers())
                      + "  soldier/s remain,  " + str(self._enemy_base.get_num_guerrillas()) +
                      "  guerrilla/s remain,  " + str(self._chopper.get_num_rescued()) + "  rescued")

        if self._enemy_base.get_num_hostages() == 0 and self._bunker.has_soldiers():
            while self._bunker.has_soldiers():
                self._chopper.board_passenger(self._bunker.deploy_next_soldier())
        # rescue final set of passengers
        if self._chopper.get_occupancy_of_chopper() > 0:
            self._chopper.rescue_passengers()

        print("Statistics:  " + str(self._enemy_base.get_num_hostages()) +
              "  hostage/s remain,  " + str(self._bunker.get_num_soldiers())
              + "  soldier/s remain,  " + str(self._enemy_base.get_num_guerrillas()) +
              "  guerrilla/s remain,  " + str(self._chopper.get_num_rescued()) + "  rescued")


def main():
    """
    Run the rescue mission simulation. The simulation requires four command-line arguments:
    1. the seed for the random number generator (positive integer)
    2. the number of hostages (positive integer)
    3. the number of soldiers (positive integer)
    4. the number of guerrillas (positive integer)

    If all arguments are supplied, it will create the rescue mission and run the simulation.
    :return: None
    """
    if len(sys.argv) < 5:
        print("Usage: python rescue_mission #_seed #_hostages #_soldiers #_guerrillas")
    else:
        _seed, _num_hostages,_num_soldiers,_num_guerrillas = sys.argv[1: 5]
        rm = Rescue_Mission(int(_seed), int(_num_hostages), int(_num_soldiers), int(_num_guerrillas))
        rm.run_simulation()


if __name__ == '__main__':
    main()
