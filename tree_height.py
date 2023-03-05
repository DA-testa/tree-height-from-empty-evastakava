# python3

import sys
import threading
import numpy


def compute_height(n, parents):

    tree = [[]for i in range (n)]
    for i, parent in enumerate(parents):
        if parent != -1:
            tree[parent].append(i)

    root = numpy.where(parents == -1)[0][0]
    q = [(root, 0)]
    max_height = 0

    while q:
        node, height = q.pop(0)
        max_height = max(max_height, height)
        for child in tree[node]:
            q.append((child, height + 1))
    return max_height + 1

def main():

    input_type = input("Enter I to input from keyboard or F to input from file: ").upper()
    if input_type[0] == "I":
        n = int(input())
        parents1 = input()
        parents = numpy.array(list(map(int, parents1.split())))
        height = compute_height(n, parents)
    elif input_type[0] == "F":
        filename = input("Enter file name: ")
        if 'a' in filename:
            print("Error. Try again.")
            return
        with open(filename, 'r') as file:
            n = int(file.readline())
            parents1 = file.readline().strip()
            parents = numpy.array(list(map(int, parents1.split())))
            height = compute_height(n, parents)

    print(height)
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))