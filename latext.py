import sys
import time

filename1 = "test.txt"
def main(filename):
    # This is without splitting lines
    # s = open(filename).read()
    # s = s.replace('\t', '*')
    # print(s)

    # This is with splittin lines
    file = open(filename)
    string = file.read().splitlines()
    print(string)
    for i in range(0, len(string)):
        string[i] = string[i].replace("\t", "*")
        print(string[i])
    print(string)



main(filename1)
