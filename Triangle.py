from __future__ import print_function

rows = input("Enter number of rows: ")
for x in range (1, rows+1):
    for y in range (0, x):
            print (x, end="")
    print("")
