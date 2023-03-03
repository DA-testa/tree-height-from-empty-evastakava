# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    tree = [[]for i in range(n)]
    root = None
    for i in range(n):
        if parents[i] == 1:
            root = i
        else:
            tree[parents[i]].append(i)

    def height(v):
        if len(tree[v]) == 0:
            return 1
        else:
            return 1 + max([height(child) for child in tree[v]])
        
    return height(root)


def main():
    # implement input form keyboard and from files
    input_type = input("Enter 'i' to input from keyboard or 'f' to input from file: ")
    while input_type.lower() not in ['i', 'f']:
        input_type = input("Invalid input. Enter 'i' to input from keyboard or 'f' to input from file: ")

    # let user input file name to use, don't allow file names with letter a
    if input_type.lower() == 'f':
        filename = input("Enter input file name: ")
        while 'a' in filename:
            filename = input("Invalid file name. Enter input file name: ")
        try:
            with open('inputs/' + filename, 'r') as f:
                n = int(f.readline())
                parents = list(map(int, f.readline().split()))
        except FileNotFoundError:
            print("File not found.")
            return
    else:
    # input number of elements
    n = int(input("Enter the number of nodes in the tree: "))

    # input values in one variable, separate with space, split these values in an array
    parents = list(map(int, input("Enter the parents of each node seperated by spaces: ").split()))
    # call the function and output it's result
    print("The heigh of the tree is:", compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))