import re


def find_emails(page_source):
    pattern = re.compile("((.+)@(.+)\\.(.+))")
    with open(page_source) as f:
        line = f.readline()
        count = 1
        while line:
            found = pattern.match(line)
            if found:
                print(found.group(0))
            line = f.readline()
            count += 1


file = input("Enter page source file name: ")
find_emails(file)
