__author__ = 'dk1346'

"""
CSCI-603: Collection (week 4)
Author: Deepika Kini

This is a program that validates the input for the skyscraper problem.
Errors such as duplicates, out-of-bound values and
invalid grid values depending on clues are shown as output,
if present

Collections used:
List for grid and it's transpose (helps to resuse code)
Named tuple and tuple for holding clue values
sets to check for duplicates in grid input


note:
Output is modeled as per output.txt files
input can be provided in the form "python3 skyscrapers.py filename"
python lab4.py /Users/deepika/Desktop/603/lab4/data/puzzle_12.txt

"""

import sys
import collections


def read_txt_file(filename):
    """
     takes file name and gets data from file
     Referred from lec notes
     :param filename: the file name and path
     """
    with open(filename) as f:
        # added 0 to get first line
        f.readline(0)
        print("\nFile:", f.name.split("/")[-1] )
        counter = 0
        list1 = []
        for line in f:
            # taking size of grid
            if counter == 0:
                size = int(line.strip())
            # taking other rows (clues and grid)
            else:
                list1.append(line.strip())
            counter += 1

        # removing the last two rows
        list1 = list1[:-2]
        compute_validity(list1, size)

def compute_validity(list1, size):
        """
         Creates separate collection and validates the grid for all cases
         :param list1: the list containing grid and clue values
         :param size: size of grid
         """
        # named tuple list for clues
        Clues = collections.namedtuple("Clues",
                                       ('Position', 'tuple'))
        top = Clues('Top', tuple(list1[0].split(" ")))
        bottom = Clues('Bottom', tuple(list1[2].split(" ")))
        right = Clues("Right", tuple(list1[1].split(" ")))
        left = Clues("Left", tuple(list1[3].split(" ")))

        # 2 d list for grid
        cols_grid = size
        rows_grid = size
        list_grid = [[0] * cols_grid] * rows_grid

        for i in range(size):
            list_grid[i] = list(list1[i + 4].replace(' ', ''))
            #print(list_grid[i])
        display(list_grid, top, bottom, left, right, size)

        # step 2a: checking if rows have duplicate
        find_duplicates(list_grid, 0, size)

        # 2 d transposed list
        list_grid_transpose = [[list_grid[j][i] for j in range(size)] for i in range(size)]
        # step 2b: checking if columns have duplicate
        find_duplicates(list_grid_transpose, 1, size)



        # Step 3: checking if values in grid correspond to provided clues
        check_violation(top[1], size, list_grid, 0, 0, size, 1, top[0])
        check_violation(bottom[1], size, list_grid, size - 1, size - 1, -1, -1, bottom[0])
        check_violation(left[1], size, list_grid_transpose, 0, 0, size, 1, left[0])
        check_violation(right[1], size, list_grid_transpose, size - 1, size - 1, -1, -1, right[0])

        #if everything goes well, print valid!
        print("The puzzle is valid!")


def check_violation(list_clue, size, list_grid, start_row, min, max, step, string_displayed):
    """
     validates the grid against the clues and exits, if non-valid
     :param list_clue: the clue that needs to be checked
     :param size: size of grid
     :param start_row: mentions if start should be from top or bottom
     :param min: min of iteration
     :param max: end of iteration
     :param step: -1 or +1 depending on direction
     :param string_displayed: the clue value in string
     """
    #declaring variables
    current_clue = list_clue
    can_see = [1 for k in range(size)]
    last_large_number = list_grid[start_row]

    for j in range(size):

        for i in range(min, max, step):
            if int(list_grid[i][j]) > int(last_large_number[j]):
                can_see[j] += 1
                last_large_number[j] = int(list_grid[i][j])

        if can_see[j] != int(current_clue[j]):

            print(string_displayed, "clue at position", j, "violated")
            sys.exit()

#not used
# def check_no_of_rows(list1, size):
#     len_of_input_rows = len(list1[4:])
#     return size == len_of_input_rows



def find_duplicates(list1, row_or_column, size):
    """
     finds duplicates if present, and exits program in such a case
     :param list1: the list that holds grid values and clues
     :param row_or_column: the flag that mentions whether row or col
     :param size: size of grid
     """
    duplicate = []
    for i in range(len(list1)):
        # hashes hence order changes
        set1 = set(list1[i])
        if len(set1) < size:
            duplicate = [building for building,
                        count in collections.Counter(list1[i]).items() if count > 1]
            #above taken from the internet
            print("Duplicate value", duplicate[0] ,"row" if row_or_column == 0 else
            "column",(i))
            sys.exit()


def display(list_grid, top, bottom, left, right,  size):
    """
     Shows the matrix and the clues in the format required
     Also validates whether grid values are the range of (1,size)
     Exits program if invalid value present
     :param list_grid: the list that holds grid values
     :param top: the top clue tuple
     :param bottom: the bottom clue tuple
     :param left: the left clue tuple
     :param right: the right clue tuple
     :param size: the size of grid
     """
    invalid_row = -1
    invalid_value = -1
    invalid_flag = 0

    print("    ", end=" ")
    for k in range(size):
        print(top[1][k], end=' ')

    print()
    print("  ", end=' ')
    for i in range(size):
        print("--", end='')
    print()
    for i in range(size):
        print(left[1][i], end=' ')
        print("|", end=' ')
        for j in range(len(list_grid[i])):
            print(list_grid[i][j], end=' ')
            if int(list_grid[i][j]) > size or int(list_grid[i][j]) < 1:
                invalid_row = i
                invalid_value = list_grid[i][j]
                invalid_flag = 1
        print("|", end=' ')
        print(right[1][i], end=' ')
        print()
    print("  ", end=' ')
    for i in range(size):
        print("--", end='')
    print()
    print("  ", end=" ")
    for k in range(size):
        print(bottom[1][k], end=' ')
    print()

    if invalid_flag == 1:
        print("Invalid value", invalid_value, "in row", invalid_row)
        sys.exit()


def main() -> None:
    """
     checks if argument is provided by user
     handles FileNotFound error
     Calls the read_txt_file method
     """
    try:
        if len(sys.argv) != 2:
            print(sys.argv[1])
        else:
            read_txt_file(sys.argv[1])
    except FileNotFoundError as fnfe:
        print(fnfe, file=sys.stderr)


if __name__ == "__main__":
    main()
