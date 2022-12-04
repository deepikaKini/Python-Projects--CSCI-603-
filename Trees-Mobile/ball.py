__author__ = 'dk1346'
import turtle
import node


class Ball(node.Node):
    __slots__ = 'radius', 'weight'
    radius: int
    weight: int

    def __init__(self, name, cord_length, radius, weight):
        super().__init__(name, cord_length)
        # self.name = name
        # self.cord_length = cord_length
        self.radius = radius
        self.weight = weight

    def __str__(self):
        """
        string rep of Ball is computed
        :return:
        """
        return "Ball(name=" + self.name + ", cord=" + str(self.cord_length) + ", radius=" + str(
            self.radius) + ", weight=" + str(self.weight) + ")";

    def get_weight(self) -> int:
        """
        weight if ball is returned
        :return: weight of ball
        """
        return self.weight

    def get_height(self) -> int:
        """
        height of ball is the cord plus the diameter
        :return: height of ball
        """
        return self.cord_length + 2 * self.radius

    def get_width(self) -> int:
        """
        total width of ball is diameter
        :return: total width
        """
        return self.get_left_width() + self.get_right_width()

    def get_left_width(self) -> int:
        """
        provides left width of ball which is radius
        :return: left width
        """
        return self.radius

    def get_right_width(self) -> int:
        """
        provides right width i.e. the radius of ball
        :return: right width
        """
        return self.radius

    def is_balanced(self) -> bool:
        """
            returns if node is balanced. ball is balanced hence returned True
            :return: boolean value of balance
        """
        return True

    def get_imbalance(self):
        """
            returns torque value. ball is abalance hence returned 0
            :return: absolute unbalanced value
        """
        # ball is balanced. torque is 0
        return 0

    def infix(self) -> str:
        """
          infix sequence of tree
          :return: string representation
        """
        return " " + self.name + " "

    def print_pretty(self, tabs: str) -> str:
        """
            prefix sequence of tree
            :param tabs: indentation
            :return: string rep of tree
        """
        return tabs + self.name

    def draw(self, t: turtle) -> None:
        """
            draws Ball  based on parameters
            :param t: turle instance
            :return: None
        """
        t.color("blue")
        t.forward(self.cord_length / 2)
        t.write("   L" + str(self.cord_length), align="right")
        t.forward(self.cord_length / 2)
        t.right(90)

        t.circle(self.radius)
        # t.penup()
        t.left(90)
        t.forward(self.radius)
        t.write("  R" + str(self.radius))
        # t.forward(self.radius)
        t.write(" " * int(self.radius / 2) + "W" + str(self.weight))

        t.backward(self.radius)
        t.write("    " + self.get_name(), align="left", font=('Courier', 10, 'bold'))

        t.right(90)
        t.pendown()

        t.right(90)
        t.forward(self.cord_length)
        return

    def find(self, name: str) -> 'Node':
        """
            finds if ball is present
            :param name: name to be found
            :return: the node if found
        """
        if self.name == name:
            return self
        else:
            return None


def test():
    b = Ball("hello", 50, 40, 60)
    print(b)
    print(b.get_name())
    print(type(b.radius))
    print(b.get_width())
    print(b.get_height())
    b.draw(turtle)
    print(b.find("hello"))
    print(b.print_pretty("\t" * 2))


if __name__ == '__main__':
    test()
