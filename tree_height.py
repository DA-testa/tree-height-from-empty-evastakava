import sys
import threading
import numpy

def compute_height(n, parents):
    tree = [[] for i in range (n)]
    for i, parent in enumerate(parents):
        if parent !=-1:
            tree[parent].append(i)
    root = numpy.where(parents == -1)[0][0]
    q = [(root,0)]
    max_height = 0;

    while q:
        node, height = q.pop(0)
        max_height = max(max_height, height)
        for child in tree[node]:
            q.append((child, height + 1))
    return max_height + 1

def main():
    text = input("Enter 'I' for input from keyboard or 'F' for input from file: ")
    if text[0] == "I":
        n = int(input("Enter the number of nodes: "))
        parents_str = input("Enter parent list: ")
        parents = numpy.array(list(map(int, parents_str.split())))
        height = compute_height(n, parents)
    elif text[0] == "F":
        filename = input("Enter file name: ")
        if "a" in filename:
            print("Error. In file name can't beletter 'a'.")
            return
        try:
            with open(filename, 'r') as file:
                n = int(file.readline())
                parents_str = file.readline().strip()
                parents = numpy.array(list(map(int, parents_str.split())))
                height = compute_height(n, parents)
        except FileNotFoundError:
            print("Error. Try again.")
            return
    else:
        print("Invalid input name.")
        return
    print(height)

if __name__ == '__main__':
    sys.setrecursionlimit(10**7)
    threading.stack_size(2**27)
    thread = threading.Thread(target=main)
    thread.start()