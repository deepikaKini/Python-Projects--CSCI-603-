__author__ = 'dk1346'

"""
CSCI-603: Search and Sort (week 5)
Author: Deepika Kini

This is a demo program that tells the optimal location to park 
food truck. It uses sorting and searching algorithm
and uses time methods to understand the time taken for 
the algorithms to compute the outcomes.
input to be provided:  
python3 food_truck.py .../test_dataset100K_odd.txt
"""

import random
import sys
import time


def read_txt_file(filename):
    """
    takes in values from input file and calculates sort and select algo
    Also uses time function to understand the time taken to compute
    :param filename: the file name provided by user
    :return: None
    """
    with open(filename) as f:
        #counter holds the number of buildings
        counter = 0
        unsorted_list = []
        for line in f:
            #take in only the distances from input file (after space)
            unsorted_list.append(int(line.split(" ")[1].strip()))
            counter += 1
        print("Number of buildings: ", counter)

        # Quick Sort calculations (time, median, dist)
        start = time.perf_counter()
        print(start)
        sorted_set_qsort = run_quick_sort(unsorted_list)
        time_elapsed = time.perf_counter() - start
        print("Using QuickSort to find optimal location")
        print("\tElapsed time:", time_elapsed, "seconds")
        median = calc_median(sorted_set_qsort, counter)
        print("\tOptimal food truck location :" ,median)
        print("\tSum of distances:", sum_of_dist(median, sorted_set_qsort, counter))

        # Quick Select calculations (time, median, dist)
        start = time.perf_counter()
        qselect = run_quick_select(unsorted_list, len(unsorted_list) // 2)
        time_elapsed = time.perf_counter() - start
        print("Using QuickSelect to find optimal location")
        print("\tElapsed time:", time_elapsed, "seconds")
        print("\tOptimal food truck location :", qselect)
        print("\tSum of distances:", sum_of_dist(qselect, unsorted_list, counter))



def run_quick_sort(unsorted_list):
    """
    Sorts the list using quick sort
    :param unsorted_list: the list to be sorted
    :return: sorted list
    """
    result = []
    if len(unsorted_list) == 0:
        return result
    else:
        less_list, equal_list, greater_list = [], [], []
        if len(unsorted_list) == 1:
            pivot = 0
        else:
            pivot = random.randint(0, len(unsorted_list) - 1)
        # print(pivot)
        for i in range(len(unsorted_list)):
            if unsorted_list[i] > unsorted_list[pivot]:
                greater_list.append(unsorted_list[i])
            elif unsorted_list[i] < unsorted_list[pivot]:
                less_list.append(unsorted_list[i])
            else:
                equal_list.append(unsorted_list[i])
        result = run_quick_sort(less_list) + equal_list + run_quick_sort(greater_list)
    return result


def run_quick_select(unsorted_list, k):
    """
    Caculates the median number using quick select
    The pivot is calculated using Random
    :param unsorted_list: the list
    :param k: the kth value to be found(in this case the median central value)
    :return: the median value
    """
    less_list, equal_list, greater_list = [], [], []
    if len(unsorted_list) == 1:
        pivot = 0
    else:
        pivot = random.randint(0, len(unsorted_list) - 1)
    for i in range(len(unsorted_list)):
        if unsorted_list[i] > unsorted_list[pivot]:
            greater_list.append(unsorted_list[i])
        elif unsorted_list[i] < unsorted_list[pivot]:
            less_list.append(unsorted_list[i])
        else:
            equal_list.append(unsorted_list[i])
    m = len(less_list)
    count = unsorted_list.count(unsorted_list[pivot])

    if k >= m and k < (m + count):
        result = unsorted_list[pivot]
    elif k < m:
        result = run_quick_select(less_list, k)
    else:
        result = run_quick_select(greater_list, k - m - count)
    return result


def calc_median(sorted_list, count):
    """
    calculates median of all points in quick sort
    Same formula irrespective of even/odd elements
    :param sorted_list: list in sorted manner
    :param count: number of elements
    :return: the median value of list
    """
    median = count // 2
    return sorted_list[median]


def sum_of_dist(median, list, count):
    """
    Calculates the sum of distances from median to different points
    :param median: the median of all points
    :param list: the list of places
    :param count: the total no. of places
    :return: sum of all distances w.r.t. median
    """
    sum = 0
    for i in range(count):
        sum += abs(median - list[i])
    return sum


def main() -> None:
    """
    the main function checks if number of parameters are good
    and if file is present as mentioned by user
    :return: None
    """
    try:
        if len(sys.argv) != 2:
            print("Usage: python3 food_truck.py input-file")
            sys.exit()
        else:
            read_txt_file(sys.argv[1])
    except FileNotFoundError as fnfe:
        print(fnfe, file=sys.stderr)


if __name__ == "__main__":
    main()
