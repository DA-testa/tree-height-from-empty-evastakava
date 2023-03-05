import sys
import threading
import numpy as np

def compute_height(n, parents):
    tree = [[] for i in range (n)]
    for i, parent in enumerate(parents):
        if parent !=-1:
            tree[parent].append(i)
    root = np.where(parents == -1)[0][0]
    queue = [(root,0)]
    max_height = 0;

    while queue:
        node, height = queue.pop(0)
        max_height = max(max_height, height)
        for child in tree[node]:
            queue.append((child, height+1))
    return max_height+1

def main():
    text = input("Enter 'I' for input from keyboard or 'F' for input from file: ")
    if text[0] == "I":
        n = int(input("Enter number of nodes: "))
        parents_str = input("Enter parent list separated by space: ")
        parents = np.array(list(map(int, parents_str.split())))
        height = compute_height(n, parents)
    elif text[0] == "F":
        file_name = input("Enter file name: ")
        if "a" in file_name:
            print("File name cannot contain letter 'a'.")
            return
        try:
            with open("folder/" + file_name, 'r') as file:
                n = int(file.readline())
                parents_str = file.readline().strip()
                parents = np.array(list(map(int, parents_str.split())))
                height = compute_height(n, parents)
        except FileNotFoundError:
            print("File not found.")
            return
    else:
        print("Invalid input option.")
        return
    print(height)

if __name__ == '__main__':
    sys.setrecursionlimit(10**7)
    threading.stack_size(2**27)
    thread = threading.Thread(target=main)
    thread.start()