#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argv_numb = len(argv)
    index = 1
    if argv_numb is 0:
        print("{} arguments.".format(argv_numb))
    elif argv_numb is 1:
        print("{} argument:".format(argv_numb))
        print("{}: {}".format(index, sys.argv[1]))
    else:
        print("{} arguments:".format(argv_numb))
        while index <= argv_numb:
            print("{}: {}".format(index, sys.argv[index]))
            index += 1
