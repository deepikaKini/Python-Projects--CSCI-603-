__author__ = 'dk1346'

import turtle
import node
from ball import Ball


# extends Node class
class Rod(node.Node):
    __slots__ = 'left_arm_length', 'left_child', 'right_arm_length', 'right_child'
    left_arm_length: int
    right_arm_length: int
    left_child: 'Node'
    right_child: 'Node'

    def __init__(self, name, cord_length, left_arm_length,
                 right_arm_length, left_child=None, right_child=None):
        super().__init__(name, cord_length)
        self.left_arm_length = left_arm_length
        self.left_child = left_child
        self.right_arm_length = right_arm_length
        self.right_child = right_child

    def __str__(self):
        """
        Returns node object in string format
        :return: string representation of Rod
        """
        return "Rod(name=" + self.name + ", cord=" + str(self.cord_length) + ", leftArm=" + \
               str(self.left_arm_length) + ", leftChild=" + self.left_child.__str__() \
               + ", rightArm=" + str(self.right_arm_length) + ", rightChild=" + self.right_child.__str__() + ")"

    def get_weight(self) -> int:
        """
        calculates weight of Rod (weigth of children balls
        :return: weight
        """
        return self.left_child.get_weight() + self.right_child.get_weight()

    def get_height(self) -> int:
        """
        returns height of node which is the max of left or right subtree
        :return: length
        """
        return self.cord_length + max(self.left_child.get_height(),
                                      self.right_child.get_height())

    def get_width(self) -> int:
        """
        returns width of tree created by node
        :return: width of node subtree
        """
        return self.get_left_width() + self.get_right_width()

    def get_left_width(self) -> int:
        """
        calculates max of left subtree or right sub tree's left part (if lopsided tree)
        example: text file 5
        :return: left width
        """
        return max(self.left_arm_length + self.left_child.get_left_width(),
                   self.right_child.get_left_width() - self.right_arm_length)
        # the other parameter for max is for one sided tree

    def get_right_width(self) -> int:
        """
               calculates max of right subtree or left sub tree's right part (if lopsided tree)
               example: text file 5
               :return: left width
        """
        return max(self.right_arm_length + self.right_child.get_right_width(),
                   self.left_child.get_right_width() - self.left_arm_length)

    def is_balanced(self) -> bool:
        """
        Returns if subtree is balanced
        :return: returns boolean value
        """
        if self.right_child.is_balanced() \
                and self.left_child.is_balanced() \
                and self.left_arm_length * self.left_child.get_weight() \
                == self.right_arm_length * self.right_child.get_weight():
            return True
        else:
            return False

    def get_imbalance(self):
        """
        returns difference between torque values of the sub trees. 0 if balanced
        :return: absolute unbalanced value
        """
        if self.is_balanced():
            return 0
        else:
            if not self.right_child.is_balanced():
                return abs(self.left_arm_length * self.left_child.get_weight()
                           - self.right_arm_length * self.right_child.get_weight())
            elif not self.left_child.is_balanced():
                return abs(self.left_arm_length * self.left_child.get_weight()
                           - self.right_arm_length * self.right_child.get_weight())
            elif self.left_arm_length * self.left_child.get_weight() \
                    != self.right_arm_length * self.right_child.get_weight():
                return abs(self.left_arm_length * self.left_child.get_weight()
                           - self.right_arm_length * self.right_child.get_weight())
            else:
                0

    def infix(self) -> str:
        """
        infix sequence of tree
        :return: string representation
        """
        return "(" + self.left_child.infix() + ") " + self.get_name() + " (" + self.right_child.infix() + ")"

    def print_pretty(self, tabs: str) -> str:
        """
        prefix sequence of tree
        :param tabs: indentation
        :return: string rep of tree
        """
        return tabs + self.get_name() + "\n" + self.left_child.print_pretty(tabs + "\t") + \
               "\n" + self.right_child.print_pretty(tabs + "\t")

    def draw(self, t: turtle) -> None:
        """
        draws Rods and the subtrees based on paramters
        :param t: turle instance
        :return: None
        """
        t.color("green")
        t.forward(self.cord_length / 2)
        t.write(" " + self.get_name(), align="left", font=('Courier', 10, 'bold'))
        t.write(" L" + str(self.cord_length), align="right")
        t.forward(self.cord_length / 2)
        t.right(90)
        t.forward(self.left_arm_length)
        t.write("L" + str(self.left_arm_length), align="left")
        t.left(90)
        self.left_child.draw(t)
        t.color("green")
        t.right(90)
        t.forward(self.left_arm_length)

        t.forward(self.right_arm_length)
        t.write("L" + str(self.right_arm_length), align="left")
        t.right(90)
        self.right_child.draw(t)
        t.color("green")
        t.left(90)

        t.forward(self.right_arm_length)
        t.right(90)
        t.forward(self.cord_length)
        return

    def find(self, name: str) -> 'Node':
        """
        finds if Rod is present else calls children nodes
        :param name: name to be found
        :return: the node if found
        """
        if self.name == name:
            return self
        else:
            found_node = self.left_child.find(name)
            if found_node is not None:
                return found_node
            else:
                return self.right_child.find(name)


def main():
    turtle.right(90)
    n = Rod("abc", 100, 100, 100, Rod("abc", 100, 100, 100, Ball("1", 100, 200, 300), Ball("1", 100, 200, 300)),
            Ball("1", 100, 200, 300))

    n.draw(turtle)
    turtle.mainloop()


if __name__ == '__main__':
    main()
