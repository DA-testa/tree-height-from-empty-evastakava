# python3

import sys
import threading
import numpy


def compute_height(n, parents):

    heights = [0] * n
    for i in range(n):
        if heights[i] == 0:
            height = 1
            parent = parents[i]
            while parent != -1:
                if heights[parent] == 0:
                    height += 1
                    parent = parents[parent]
                else:
                    height += heights[parent]
                    break
            heights[i] = height

    return max(heights)


def main():

    source = input("Enter 'I' to input from keyboard or 'F' to input from file: ")
    while source not in ['I', 'F']:
        source = input("Invalid input.")
    if source == "I":
        n = int(input())
        parents = list(map(int, input().split()))
    else:
        filename = input("Enter file name: ")
        while 'a' in filename not in filename:
            filename = input("Invalid file name. Enter again: ")
        try:
            with open("input/" + filename, "r") as f:
                n = int(f.readline().strip())
                parents = list(map(int, f.readline().split()))
        except FileNotFoundError:
            print("File not found.")
            return
    height = compute_height(n, parents)   
    print(height)
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))