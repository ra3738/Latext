filename1 = "test.txt"
def main(filename):
    file = open(filename)
    string = file.read().splitlines()
    print(string)



main(filename1)