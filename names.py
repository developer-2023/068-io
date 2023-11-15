# docs.python.org/3/library/functions.html#open
# 7:27:12 Harvard CS50’s Introduction to Programming with Python – Full University Course

# "r" omitted
with open("names.txt") as file:
    for line in sorted(file, reverse=True):
        print("hello, ", line.rstrip())