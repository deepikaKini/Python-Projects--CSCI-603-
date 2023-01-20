__author__ = 'dk1346'

"""
CSCI-603: Pond (Lab 9: Graphs)
Author: Deepika Kini
The below code solves the problem of getting out of a frozen pond and reaching the exit
This works on the Graph data structure which uses the underlying concepts of Adjacency list
for keeping track of the neigbours &
the Shortest Path / Breadth First Search algorighm to traverse through the list
Reused and modified code of Subway, Vertex, Graph files shared in lecture code
"""
import os.path
import sys
from graph import Graph
from searchAlgos import canReachDFS, findPathDFS, findShortestPath


class Pond:
    """
    The class helps deal with the frozen pond situation
    """
    __slots__ = 'graph', 'height', 'width', 'exit', 'stored_input'

    def __init__(self, filename):
        """
        Construct the pond and initialise the variables
        :param filename (str): The input file (test1/2/3.txt)
        :return: None
        """

        # initialize structures and taking in the input text file
        self.graph = Graph()
        with open(filename) as f:
            self.height, self.width, self.exit = f.readline().strip().split(" ")
            self.height, self.width, self.exit = int(self.height), int(self.width), int(self.exit)

            # the list where the txt file is stored
            self.stored_input = []
            for line in f:
                # stopping when empty line encountered
                if line.strip() == "":
                    break
                # append since it should be a 2d matrix
                self.stored_input.append(line.strip().split(" "))

    def __str__(self):
        """
        Return a string representation of the graph's adjacency list, e.g.:
            Node0: ['Node1', 'Node2']
            Node1: ['Node0']
            ...
        :return: The string for the graph
        """
        result = ''
        for node in self.graph:
            result += str(node.id) + ': '
            result += str([neighbor.id for neighbor in node.getConnections()])
            result += '\n'
        return result

    def create_graph(self):
        """
        Makes the graph and calls the
        method that generates required output
        :return: None
        """

        self.add_vertices()
        self.create_edges()
        self.display_output()


    def add_vertices(self):
        """
        This adds the required vertices to the graph and an additional vertex: the exit
        :return: None
        """
        for i in range(len(self.stored_input)):
            for j in range(len(self.stored_input[i])):
                if self.stored_input[i][j] == ".":  # stones are not vertices hence ignoring the * blocks
                    # adding vertex/node in the form of index(col,row) of block in graph
                    self.graph.addVertex((j, i))
        # adding details of the exit node and linking it to the main graph
         #if node that is attached to the exit node is a viable square, then add edge
        if self.stored_input[self.exit][self.width - 1] == ".":
            self.graph.addEdge((self.width - 1, self.exit), (self.width, self.exit))
        else:
            # else add only vertex of exit node(unreachable)
            self.graph.addVertex((self.width, self.exit))

    def create_edges(self):
        """
        Using the logic of going through the grid until a pond border/stone is encountered,
        all directions are pursued for each and every node.
        This method helps call the 4 methods (each direction) and created edges for each node
        if it has a link to the extremes
        :return: None
        """
        # iterating through the graph nodes
        for key_name in self.graph:
            key = key_name.id

            # adding the edge with the node in the right
            if self.go_ahead(key) != None:
                connected_node = self.go_ahead(key)
                self.graph.addEdge(key, connected_node)
            # adding the edge with the node in the left
            if self.go_back(key) != None:
                connected_node = self.go_back(key)
                self.graph.addEdge(key, connected_node)
            # adding the edge with node which is below
            if self.go_down(key) != None:
                connected_node = self.go_down(key)
                self.graph.addEdge(key, connected_node)
            # adding the edge with node which is on top
            if self.go_up(key) != None:
                connected_node = self.go_up(key)
                self.graph.addEdge(key, connected_node)

    def go_ahead(self, current_coordinate):  # goes right towards the exit
        """
        This method goes to the max limit of the right to get a node to be linked
        to caller node(current_coordinate)
        :param current_coordinate: the caller node
        :return: Extreme node which is in front of the caller node
        """
        i, j = current_coordinate
        k = i
        # if k is less than width and the vertex is present (not a rock)
        while k < self.width - 1 and self.graph.getVertex((k + 1, j)):
            k += 1

        # edge case where row is the exit row
        if j == self.exit and k == self.width - 1:
            k += 1
            #returns None if no movement can be made
        if k != i:
            return (k, j)

    def go_back(self, current_coordinate):
        """
        This method goes to the max limit of the left to get a node to be linked
        to caller node(current_coordinate)
        :param current_coordinate: the caller node
        :return: Extreme node which is behind the caller node
        """
        i, j = current_coordinate
        k = i
        while k > -1 and self.graph.getVertex((k - 1, j)):
            k -= 1

        if k != i:
            return (k, j)

    def go_down(self, current_coordinate):
        """
        This method goes to the max limit below and provides a node to be linked
        to caller node(current_coordinate)
        :param current_coordinate: the caller node
        :return: Extreme node which is below the caller node
        """
        i, j = current_coordinate
        k = j
        while k < self.height - 1 and self.graph.getVertex((i, k + 1)):
            k += 1

        if k != j:
            return (i, k)

    def go_up(self, current_coordinate):
        """
            This method goes to the max limit above and provides a node to be linked
            to caller node(current_coordinate)
            :param current_coordinate: the caller node
            :return: Extreme node which is above the caller node
        """
        i, j = current_coordinate
        k = j
        while k > -1 and self.graph.getVertex((i, k - 1)):
            k -= 1

        if j != k:
            return (i, k)

    def display_output(self):
        """
        The output should be of format:
        1: [(node1),(node2)]
        2: [(node3)]
        no path : [(node 4)]
        and so on where the left hand of equation indicates the no. of steps/hops
        it takes for the corresponding nodes in the list to reach the exit.
        The method deals with getting the BFS path for each node and saving the number
        of hops and the node in dictionary
        :return: None
        """
        hops_to_exit = {-1: []}
        for node in self.graph:
            startVertex = node
            endVertex = self.graph.getVertex((self.width, self.exit))
            # getting shortest route between each node and exit using BFS logic
            path = findShortestPath(startVertex, endVertex)
            # no path exists, append to list associated to key -1
            if path == None:
                hops_to_exit[-1].append(node.id)
            else:
                # if path exists, append node to key which is no. of hops
                if (len(path) - 1) not in hops_to_exit.keys():
                    # if key not present
                    hops_to_exit[len(path) - 1] = []
                # append node to list of corresponding hop value
                hops_to_exit[len(path) - 1].append(node.id)
        # sort keys using sort method applicable to dictionary
        for i in sorted(hops_to_exit.keys()):
            if i != 0 and i != -1:
                # print nodes with hop value greater than 0
                print(str(i) + ": ", hops_to_exit[i])
        # print nodes with no path
        print("No path: " + str(hops_to_exit[-1]))


def main():
    """
    The main function prompts for the file name and
    initiates the steps
    :return: None
    """
    try:
        # creating an instance of pond and calling methods to construct and
        # traverse the graph to reach the exit
        pond_instance = Pond(sys.argv[1])
        pond_instance.create_graph()



    # if error with file name
    except IOError as err:
        print(err)


if __name__ == '__main__':
    main()


