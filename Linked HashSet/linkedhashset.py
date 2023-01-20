__author__ = 'dk1346'

"""
CSCI-603: Lab 7 (LinkedHashSet implementation for hashing Lab) 
Author: Deepika Kini

This is a program implements a linked Hash Set with links to 
not just next node in the bucket as per chained hashing but also pointers
to next and previous nodes as per the initial sequence

Note:
 load_limit is considered to be an instance variable
"""

from typing import Any
import collections
import set
from collections.abc import Iterable, Iterator


class ChainNode:
    __slots__ = "obj", "prev", "fwd", "next"
    obj: Any
    prev: "ChainNode"
    next: "ChainNode"
    fwd: "ChainNode"

    def __init__(self, obj: Any, prev: "ChainNode" = None, fwd: "ChainNode" = None, next: "ChainNode" = None) -> None:
        self.obj = obj
        self.fwd = fwd
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        """ Return a string representation of the contents of
            this node. The link is not included.
        """
        return str(self.obj)

    def __repr__(self) -> str:
        """ Return a string that, if evaluated, would recreate
            this node and the node to which it is linked.
            This function should not be called for a circular
            list.
        """
        return repr(self.obj) + " -> " + repr(self.fwd)


MIN_BUCKETS = 10


class LinkedHashSet(set.SetType, collections.abc.Iterable):
    __slots__ = "initial_num_buckets", "load_limit", "table", "front", "back", "hash_function"
    initial_bucket: int
    load_limit: float
    table: ["ChainNode"]  # check if this is right!!
    hash_function: int
    front: "ChainNode"
    back: "ChainNode"

    def __init__(self, initial_num_buckets: int = 100, load_limit: float = 0.75, hash_function = hash) -> None:
        assert initial_num_buckets >= MIN_BUCKETS, "Min bucket size is 10"
        # To initialize the instance field 'size' inherited from the SetType class, You must call
        # the super's constructor
        super().__init__()
        # initialising the three instance variables of LinkedHashSet
        self.initial_num_buckets = initial_num_buckets
        self.load_limit = load_limit
        self.table = [None] * self.initial_num_buckets
        self.front = None
        self.back = None
        self.hash_function = hash_function

    def __len__(self) -> int:
        return self.size

    class _Iter:
        # iterates from front to back (in insertion sequence)
        __slots__ = 'cursor', 'the_list'
        cursor: 'ChainNode'
        the_list: 'LinkedHashSet'

        def __next__(self) -> Any:
            if self.cursor is None:
                raise StopIteration()
            else:
                result = self.cursor
                self.cursor = self.cursor.next
            return result

    def __iter__(self) -> Iterator[Any]:
        """
        Build an iterator.
        :return: an iterator for the current elements in the set
        """
        result = LinkedHashSet._Iter()
        result.the_list = self
        result.cursor = self.front
        return result

    def __repr__(self):
        """
        Return a string with the content of the hash table and information about the hash table such as
        the table's capacity, size, current load factor and load limit.
        """
        print("\n OUTPUT")
        print(" -----")
        print("Capacity: " + str(self.initial_num_buckets) + ", Size: " + str(self.__len__()) + ", Load Factor: " + str(
            self.size / self.initial_num_buckets) + ", Load Limit: " + str(self.load_limit))
        print("\tHash Table")
        print("\t----------")
        # below uses iter method
        cursor = 0
        while cursor < len(self.table):
            print("\t" + str(cursor) + ": " + self.table[cursor].__repr__())
            cursor = cursor + 1

    def __str__(self):
        """
        Return a string representation of the objects added to this set sorted by insertion order.
        The string will contain all the objects separated by comma and enclosed between curly braces.
        Example:
            "{obj1, obj2, obj3, ...}"
        """
        node = self.front
        return_string = "{"
        while node is not None:
            return_string += node.__str__()
            node = node.next
        return_string += "}"
        return return_string


    def add(self, obj) -> bool:
        """
        Insert a new object into the hash table and remember when it was added
        relative to other calls to this method. However, if the object is
        added multiple times, the hash table is left unchanged, including the
        fact that this object's location in the insertion order does not change.
        Double the size of the table if its load_factor exceeds the load_limit.
        param obj: the object to add
        return: True iff obj has been added to this set
        """
        # latest_added_node
        #obj = str(obj)
        hashed_address = self.hash_function(obj) % self.initial_num_buckets
        new_node = ChainNode(obj)
        if self.front is None:
            # no elements in the hashset, adding first element to bucket
            self.front = self.back = new_node
            self.table[hashed_address] = new_node

            self.size += 1
            return True
        else:
            # some element present
            if self.table[hashed_address] is None:
                # if bucket is empty, add first element of bucket
                self.table[hashed_address] = new_node
            else:
                # nodes present in the bucket
                # node represents the temp node to traverse
                # walker
                walker = self.table[hashed_address]
                prev_node_walker = walker
                while walker is not None:
                    if walker.obj == new_node.obj:
                        # duplicate already present hence return false
                        return False
                    else:
                        # traversing to last element
                        prev_node_walker = walker
                        walker = walker.fwd
                # reached last element
                prev_node_walker.fwd = new_node
            # updating the back node and the prev node's next ptr
            self.back.next = new_node
            new_node.prev = self.back
            new_node.fwd = None
            self.back = new_node
            # incrementing size of data elements in LHS
            self.size += 1

            # if size is beyond threshold, resize and rehash
            load_factor = self.size / self.initial_num_buckets
            if load_factor > self.load_limit:
                self.resize_check("increase")
            return True

    def contains(self, obj) -> bool:
        if self.front is None:  # if empty
            return False
        else:

            # if linkedhashset not empty
            #obj = str(obj)
            hashed_address = self.hash_function(obj) % self.initial_num_buckets

            # if bucket empty
            if self.table[hashed_address] is None:
                return False
            # if not empty, initialise walker to traverse nodes at bucket
            else:
                walker = self.table[hashed_address]
                while walker is not None:
                    if walker.obj == obj:
                        return True
                    else:
                        # go to next node
                        walker = walker.fwd
                # didn't find object
                return False

    def remove(self, obj):
        if self.contains(obj) is False:
            return False
        #obj = str(obj)
        hashed_address = self.hash_function(obj) % self.initial_num_buckets
        walker = self.table[hashed_address]
        prev_node_walker = walker
        while walker is not None:
            # node represents the temp node to traverse
            if walker.obj == obj:#found object
                if self.table[hashed_address].obj == obj:  # first node of bucket
                    self.table[hashed_address] = walker.fwd
                else:#not first node. handles nulls in fwd
                    prev_node_walker.fwd = walker.fwd
                # handling first node deletion
                if self.front.obj == walker.obj:
                    self.front = walker.next#will point to None if empty
                    if walker.next is not None:#next node's prev points to None, if next present
                        walker.next.prev = None
                # handling last node deletion
                elif self.back.obj == walker.obj:
                    self.back = walker.prev
                    if walker.prev is not None:
                        walker.prev.next = None

                else: #nodes in between front and back
                    print(walker.prev.obj)
                    print(walker.next.obj)
                    walker.prev.next = walker.next
                    walker.next.prev = walker.prev

                self.size -= 1

                #checking if size decrease is requried
                if self.size < ((1 - self.load_limit) * self.initial_num_buckets):
                    self.resize_check("decrease")
                    # self.resize_check()#implement this for downsizing
                return True
            else:
                #not found object, hence traverse
                prev_node_walker = walker
                walker = walker.fwd
        return False

    def resize_check(self, instruction):
        """
        depending on where call comes from (add or delete function,
        it sets the new object parameters and then calls the rehashing
        function
        :param instruction: flag to indicate whether the size has to be
        increased or decreased
        :return: None
        """
        if instruction == "increase":
            new_list = LinkedHashSet(self.initial_num_buckets * 2, hash_function=self.hash_function)
            # updating the bucket size
            self.initial_num_buckets *= 2

        elif instruction == "decrease" and self.initial_num_buckets // 2 >= MIN_BUCKETS:
            new_list = LinkedHashSet(self.initial_num_buckets // 2, hash_function=self.hash_function)
            # updating the bucket size
            self.initial_num_buckets = self.initial_num_buckets // 2
        else:
            new_list = LinkedHashSet(MIN_BUCKETS, hash_function=self.hash_function)
            # updating the bucket size
            self.initial_num_buckets =MIN_BUCKETS

        print("REHASHED to size", self.initial_num_buckets)
        self.rehash_table(new_list)


    def rehash_table(self, new_list):
        """
        rehashes old table elements' to new table
        and assigns to the old object
        :param new_list: the new list
        :return: None
        """
        # reshashing old elements into new table
        # updating table
        for i in self:  # Important change
            # reshashing present elements
            new_list.add(i.obj)
        self.table = new_list.table
        self.front = new_list.front
        self.back = new_list.back
        #("front and back of new table:", self.front, self.back, self.initial_num_buckets, self.table)





