"""

An abstraction for any class that represent
a type of node in a mobile.

Author: RIT CS
"""
__author__ = 'CS RIT'

from abc import abstractmethod, ABCMeta
from turtle import Turtle

class Node(metaclass=ABCMeta):
    """
    Represent a node in the mobile. Every node regarding its type has:
    - a name
    - a cord length
    """
    __slots__ = "name", "cord_length"
    name: str
    cord_length: int

    def __init__(self, name: str, cord_length: int):
        """
        This abstract class only keeps that state information about the name
        and the cord length of the node.
        :param name: the name
        :param cord_length: the cord length
        """
        self.name = name
        self.cord_length = cord_length

    def get_name(self) -> str:
        """
        Get the node's name.
        This is a non-abstract method.
        :return: the name
        """
        return self.name

    @abstractmethod
    def get_weight(self) -> int:
        """
        Get the node's weight
        :return: the weight
        """
        return -1

    @abstractmethod
    def get_height(self) -> int:
        """
        Get the node's height
        :return: the height
        """
        return -1

    @abstractmethod
    def get_width(self) -> int:
        """
        Get the total node's width
        :return: the total width
        """
        return -1

    @abstractmethod
    def get_left_width(self) -> int:
        """
        Get the total width of the left child
        :return: the left width
        """
        return -1

    @abstractmethod
    def get_right_width(self) -> int:
        """
        Get the total width of the right child
        :return: the right width
        """
        return -1

    @abstractmethod
    def is_balanced(self) -> bool:
        """
        Whether the node is balanced
        :return:
        """
        return False

    @abstractmethod
    def get_imbalance(self):
        """
        Get the node's amount of imbalance.
        Imbalance is the different between its left and right torques.
        :return: the node's imbalance.
        """
        return 0

    @abstractmethod
    def infix(self) -> str:
        """
        Get a infix string representation of the node
        :return: the infix string
        """
        return ""

    @abstractmethod
    def print_pretty(self, tabs: str) -> str:
        """
        Get a preorder string representation of the node
        :param tabs: the indentation level
        :return: the preorder string
        """
        return ""

    @abstractmethod
    def draw(self, t: Turtle) -> None:
        """
        Draw the node using Turtle.
        :pre: pen down, facing south, position: top of the node's cord
        :post: pen down, facing south, position: top of the node's cord
        :param t: the turtle's instance
        :return: None
        """
        pass

    @abstractmethod
    def find(self, name: str) -> 'Node':
        """
        Find a node by name
        :param name: the node's name
        :return: the node or None
        """
        return None
