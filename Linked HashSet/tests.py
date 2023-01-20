"""
file: tests.py
description: Verify the LinkedHashSet class implementation
Also contains testing hash function
"""

__author__ = "dk1346"

from linkedhashset import LinkedHashSet
from typing import Any
def print_set(a_set):
    for word in a_set:  # uses the iter method
        print(word, end=" ")
    print()


def test0():
    """
    general test to add words and test repr and iterator outputs
    using inbuilt hash
    halves the size when removing element
    using generated hash function
    :return: None
    """

    table = LinkedHashSet(100, hash_function=hash_function)
    table.add("to")
    table.add("do")
    table.add("is")
    table.add("to")
    table.add("be")

    print_set(table)

    print("'to' in table?", table.contains("to"))
    table.remove("to")
    print("'to' in table?", table.contains("to"))
    # print("'is' in table?", table.contains("is"))
    # table.remove("is")
    table.__repr__()
    print("Iterator:")
    print_set(table)


def hash_function(string_input: Any) -> int:
    """ self created hash function for testing.
        the function sums up the ordinal values of the
         characters scaled by 31 to the power of the index
         at which that character occurs in the string
         :return: int value of the formula
    """
    hashcode = 0
    iterator_var = 0
    for i in str(string_input):
        hashcode += ord(i) * 31 ** iterator_var
        iterator_var += 1
    address = hashcode
    return address

def test1():
    """
    test case for checking the rehashing of a table when adding many elements
    also tests adding duplicates
    rehashed in bigger tables twice- once at 37th element and other at 75th (0.75 threshold)

    :return:None
    """
    table = LinkedHashSet(50)
    print("\n______ADDING________")
    for i in range(87):
        print("added element", i, "?:", table.add(i))
    table.__repr__()
    #adding duplicates. output should be false
    print("\n______ADDING DUPLICATES________")

    for i in [1,4,72]:
        print("added element ", i, "?:", table.add(i))
    print("Iterator:")
    print_set(table)



def test2():
    """
   test case for checking the rehashing of a table when adding many elements
    also tests adding duplicates
    rehashed 4 times- increased size at 37th element and decreased size 3 times
   :return: None
    """
    table = LinkedHashSet(50)
    print("\n______ADDING________")
    for i in range(50):
        print("added element", i, "?:", table.add(i))
    table.__repr__()
    # adding duplicates. output should be false
    print("\n______ADDING DUPLICATES________")

    for i in [1, 4, 72, 89]:#72 isn't duplicate so is added
        print("added element ", i, "?:", table.add(i))
    print("Iterator:")
    print_set(table)

    print("\n______CONTAINS________")
    for i in [1, 89, 72, 83]:  # 72 isn't duplicate so is added
        print("element ", i, "present?:", table.contains(i))


    print("\n______REMOVING________")

    for i in range(49):
        print("removed element", i, "?:", table.remove(i))
    # should have values from 51 to 74(size 24)
    print("Iterator:")
    print_set(table)
    table.__repr__()
    # print(table.__len__())


def test3():
    """
    adding and removing all elements
    the capacity doesn't fall below MIN_BUCKET
    :return: None
    """

    table = LinkedHashSet(50)
    print("\n______ADDING________")
    for i in range(50):
        print("added element", i, "?:", table.add(i))
    table.__repr__()
    print("\n______REMOVING________")

    for i in range(50):
        print("removed element", i, "?:", table.remove(i))
    # should have values from 51 to 74(size 24)
    print("Iterator:")
    print_set(table)
    table.__repr__()
    # print(table.__len__())


if __name__ == '__main__':
    print("++++++++++++++++++ TEST 1 ++++++++++++++++")
    test0()
    print()
    print("++++++++++++++++++ TEST 2 ++++++++++++++++")
    test1()
    print()
    print("++++++++++++++++++ TEST 3 ++++++++++++++++")
    test2()
    print()
    print("++++++++++++++++++ TEST 4 ++++++++++++++++")
    test3()


