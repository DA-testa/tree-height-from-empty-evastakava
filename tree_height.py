# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    nodes = [[]for i in range(n)]
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            nodes[parents[i]].append(i)

    height = 0
    q = [root]
    while q:
        height += 1
        next_level = []
        for v in q:
            next_level += nodes[v]
        q = next_level
    return height


def main():

    input_type = input("Enter 'I' to input from keyboard or 'F' to input from file: ")

    if input_type == 'I':

        n = int(input("Enter the number of nodes: "))
        parents = list(map(int, input("Enter the parents of nodes seperated by space: ").split()))

    elif input_type == 'F':

        filename = input("Enter the name of the input file: ")
        if 'a' in filename:
            print("Invalid filename.")
            return
        try:
            with open(f'./{filename}', 'r') as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
        except FileNotFoundError:
            print("File not found. Please try again.")
            return
        
    else:
        print("Invalid input type. Please enter 'I' or 'F'. ")
        return

    height = compute_height(n, parents)
    # call the function and output it's result
    print(height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))