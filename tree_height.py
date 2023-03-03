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
    stack = [(root, 1)]
    while stack:
        node, level = stack.pop()
        height = max(height, level)
        for child in nodes[node]:
            stack.append((child, level+1))
    return height


def main():

    input_type = input("Enter 'I' to input from keyboard or 'F' to input from file: ").lower()
    while input_type not in ['i', 'f']:
        print("Invalid input type. Please enter I or F")
        input_type = input("Enter 'I' to input from keyboard or 'F' to input from file: ").lower()

    if input_type == 'i':
        n = int(input())
        parents = list(map(int, input().split()))
    else:
        filename = input("Enter input file name: ")
        while 'a' in filename:
            print("Invalid file name. Please try again.")
            filename = input("Enter input file name: ")
        try:
            with open(f"folder/{filename}", 'r') as f:
                n = int(f.readline())
                parents = list(map(int, f.readline.split())))
        except FileNotFoundError:
            print("File not found. Please try again.")
            return
        

    tree_height = compute_height(n, parents)

    print(tree_height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))