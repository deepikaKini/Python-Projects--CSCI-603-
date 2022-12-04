__author__ = 'dk1346'

"""
CSCI-603: Mobile (Lab 8: Trees)
Author: Deepika Kini

This program generates a mobile which has nodes as nodes and balls (leaf nodes).
Using abstract class Node, it enforces methods onto the Rod and Ball classes 
which implements them according to the requirement.
Recursion is used in multiple methods to traverse.
The tree is constructed using txt files.
The user needs to put in commands to get the outputs.
Turtle is used to see how to tree is visualised
"""
import os.path
import sys
from node import Node
from rod import Rod
from ball import Ball
import turtle as t


# draw, clean the code and comment
def read_txt_file(filename):
    """
    Reads the tree nodes from text file and calls required methods
    :param filename: the text file for tree generation
    :return: None
    """
    with open(filename) as f:
        fname = f.name.split("/")[-1]
        # print("\nFile:", fname)
        counter = 0
        # the list where the txt file is stored
        store_input = []
        for line in f:
            # stopping when empty line encoutered
            if line.strip() == "":
                break
            store_input.append(line.strip())
            counter += 1
        # print(store_input)
        print("Welcome to Mobiles App!\n" + \
              fname + " loaded and parsed!", end=" ")
        print()
        # parse the input to create the data structure
        root_node = parse(store_input, 0)
        take_user_input(root_node, fname)


def take_user_input(root_node, fname):
    # run the loop of taking user inputs
    while True:
        # user input format : cmd node_name(optional)
        input_cmd = str(input()).split(" ")
        print(">", end=" ")
        match input_cmd[0]:
            case 'root':
                draw_root(root_node)
            case 'quit':
                print("Bye!", end = "")
                sys.exit(0)
            case 'help':
                help_user()
            case 'balanced':
                print(root_node.get_name() + " balanced? " + balanced(root_node))
            case 'print':
               print(print_tree(root_node))
            case 'infix':
                print(infix1(root_node))
            case 'find':
                found_node = root_node.find(input_cmd[1])
                if found_node != None:
                    print("Found:", found_node)
                else:
                    print(input_cmd[1] + " not found")
            case 'weight':
                print(weight_node(root_node, input_cmd[1]))
            case 'height':
                print(height_node(root_node, input_cmd[1]))
            case 'width':
                print(width_node(root_node, input_cmd[1]))
            case 'draw':
                draw(root_node, fname)
            case default:
                # print all commands if user input does not conform
                print("Unknown command: " + input_cmd[0])


def parse(input_list, current_node_index) -> 'Node':
    """
    parses the text input which contains nodes in preorder manner, into a tree
    in a recursive manner
    :param input_list:  the list
    :param current_node_index: the current index to be computed in list
    :return: the root node
    """
    # for recursive condition of rod
    if input_list[current_node_index].startswith('R'):
        node_parameters = input_list[current_node_index].split(" ")
        new_node = Rod(node_parameters[1], int(node_parameters[2]), int(node_parameters[3]),
                       int(node_parameters[4]), parse(input_list, current_node_index + 1))
        # print(number_of_nodes_of_left_subtree(new_node.left_child))
        # use the count of left tree nodes to get the index of right tree index in the list
        new_node.right_child = parse(input_list, current_node_index + 1 +
                                     number_of_nodes_of_left_subtree(new_node.left_child))
        return new_node
    else:  # base condition ie the ball
        node_parameters = input_list[current_node_index].split(" ")
        return Ball(node_parameters[1], int(node_parameters[2]), int(node_parameters[3]),
                    int(node_parameters[4]))


def number_of_nodes_of_left_subtree(node):
    """
    This method is used by the parse method to compute
    the right tree node's index in txt file
    :param node: the left child of parent whose right node's index needs to be found
    :return: count of nodes in left subtree
    """
    if node is None:
        return 0
    elif str(node)[0] == 'B':
        return 1
    else:
        return 1 + number_of_nodes_of_left_subtree(node.left_child) + number_of_nodes_of_left_subtree(node.right_child)


def help_user():
    """
    lists all the commands to user
    :return: None
    """
    list_cmds = {'help':"this help message",
                 'quit': "end the program",
                 'root':  "display the root node of the mobile",
                 'balanced': "is the mobile balanced or not?",
                 'print':"pretty print the nodes in the mobile in preorder fashion",
                 'infix':"get an infix list of the nodes in the mobile",
                'find node':"find and display a node in the mobile ",
                 'weight node':"find the weight of a node in the mobile",
                'height node':"find the height of a node in the mobile",
                'width node':"find the width of a node in the mobile",
                'draw':"draw the mobile"}
    [print(key +":", value) for key,value in list_cmds.items()]


def draw_root(root):
    """
    Prints the root and it's parameters in recursive fashion
    :param root: the root of tree
    :return:
    """
    print("Root:", root)


def balanced(root):
    """
    Checks if tree is balanced (i.e. torque is 0) and provides imbalance
    :param root: the root of tree
    :return: the string representation of is_balanced and the imbalance value
    """
    return str(root.is_balanced()) + "\nImbalance amount: " + str(root.get_imbalance())


def print_tree(node):  # can't overwrite already present print()
    """
    prints the pre-order of tree in an indented form
    :param node: root node
    :return:
    """
    return node.print_pretty("\t" * 0)


def weight_node(root, node_name):
    """
    searches and obtains the node pointer and
    returns the weight of the node(which includes weight of children)
    :param root: the root
    :param node_name: the node for which weight is required
    :return: string representation of weight
    """
    node = root.find(node_name)
    if node is not None:
        return node.get_name() + " weight? " + str(node.get_weight())


def height_node(root, node_name):
    """
       searches and obtains the node pointer and
       returns the height of the subtree of node
       :param root: the root
       :param node_name: the node for which height is required
       :return: string representation of height
    """
    node = root.find(node_name)
    if node is not None:
        return node.get_name() + " height? " + str(node.get_height())


def width_node(root, node_name):
    """
       searches and obtains the node pointer and
       returns the width of subtree and left and right parts of node
       :param root: the root
       :param node_name: the node for which width is required
       :return: string representation of width
    """
    node = root.find(node_name)
    if node is not None:
        return node.get_name() + " width? " + str(node.get_width()) + \
               "\n" + node.get_name() + " left width? " + str(node.get_left_width()) + \
               "\n" + node.get_name() + " right width? " + str(node.get_right_width())


def draw(root, fname):
    """
    draws the tree using draw methods in the node classes
    :param root: the root node of tree
    :return: None
    """
    t.setheading(0)
    t.title('Mobile : ' + fname)
    t.speed(0)  # avoid animation
    t.setup(root.get_width() * 2, root.get_height() * 1.3)  # set window size
    #t.penup()
    #t.left(90)
    # t.fillcolor("blue")
    #
    # t.forward(root.get_height() / 2)
    # t.left(90)
    # t.forward(root.get_width() / 3 / 4)
    t.hideturtle()
    t.right(90)
    t.right(180)
    t.penup()
    t.goto(0,root.get_height() * 0.6)
    t.pendown()
    t.right(180)

    #
    # t.hideturtle()
    # t.pendown()
    # t.right(180)  # facing south
    root.draw(t)  # draw root
    t.mainloop()


def infix1(node) -> str:
    """
    prints the tree in infix manner
    :param node: the root
    :return: string representation of inorder sequence
    """
    return "(" + node.infix() + ")"


def main():
    """
    the main method which takes the arguments (filename) and checks for error
    :return: None
    """
    if len(sys.argv) < 2:
        # filename argument not provided
        print("Usage: python mobile <mobile-file>")
        sys.exit(0)
    else:
        # file not present
        filename = sys.argv[1]
        print(filename)
        if not os.path.isfile(filename):
            print("File not found: ", filename)
            sys.exit(0)
        else:
            # no error - read file
            read_txt_file(filename)


if __name__ == '__main__':
    main()
