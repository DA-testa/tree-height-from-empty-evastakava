# python3

import sys
import threading
import numpy


def compute_height(n, parents):

    tree = [[]for i in range(n)]

    for i, parent in enumerate(parents):
        if parent != -1:
            tree[parent].append(i)

    root = numpy.where(parents == -1)[0][0]
    queue = [(root, 0)]
    max_height = 0

    while queue:
        node, height = queue.pop(0)
        max_height = max(max_height, height)
        for child in tree[node]:
            q.append((child, height + 1))
    return max_height + 1

def main():

    input_type = input("Enter I to input from keyboard or F to input from file: ").upper()
    if input_type[0] == "I":
        n = int(input("Enter the number of nodes: "))
        parents_input = input("Enter the parents list: ")
        parents = numpy.array(list(map(int, parents_input.split())))
        height = compute_height(n, parents)
    elif input_type[0] == "F":
        filename = input("Enter file name: ")
        if 'a' in filename:
            print("Error. File name contains the letter 'a'. Please try again.")
            return
        try:
            with open(filename, 'r') as file:
                n = int(file.readline())
                parents_input = file.readline().strip()
                parents = numpy.array(list(map(int, parents_input.split())))
                height = compute_height(n, parents)
        except FileNotFoundError:
            print("Error.")
            return
    else:
        print("Invalid input type")
        return
    print(height)


if __name__ == '__main__':
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    thread = threading.Thread(target=main)
    thread.start()
    # print(numpy.array([1,2,3]))