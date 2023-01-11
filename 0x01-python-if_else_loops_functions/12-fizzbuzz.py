#!/usr/bin/python3
def fizzbuzz():
    '''Prints the numbers from 1 to 100'''
    for numbers in range(1, 101):
        if numbers % 3 == 0:
            print("Fizz ", end="")
        elif numbers % 5 == 0:
            print("Buzz ", end="")
        elif numbers % 3 == 0 and numbers % 5 == 0:
            print("FizzBuzz ", end="")
        else:
            print("{} ", end="")
