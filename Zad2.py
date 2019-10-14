import re

def validate(file):
    pattern = re.compile("^(.+);([0-9]+);([0-9]+)$")
    with open(file) as f:
        line = f.readline()
        while line:
            found = pattern.match(line.rstrip())
            if found:
                line = f.readline()
            else:
                print("Wrong formatting")
                return
    print("Correct formatting")

file = 'file.csv'
validate(file)

