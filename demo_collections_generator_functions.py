#! /bin/python
# Name:        demo_collections_generator_functions.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate how to generate a collection of
# numbers using generator functions.
# Why and when to use generator functions:
#    https://realpython.com/introduction-to-python-generators/
"""
    Generate and display collection of numbers lazily...
"""
import sys

def get_numbers():
    """ Return an ENTIRE list of numbers """
    print("Executing get_numbers()..")
    numbers = []
    for x in range(0, 11, 1):
        if x % 2 == 0:
            numbers.append(x)
    return numbers

def generate_numbers():
    """ GENERATE one object/number at a time = Lazy List """
    print("Executing generate numbers()..")
    for  x in range(0, 11, 1):
        if x%2 == 0:
            yield x

def generate_numbers2():
    """ GENERATE one object/number at a time = Lazy List
        using a return and list comprehension, eek! """
    print("Executing generate numbers2()..")
    return( x for x in range(0, 11) if x%2==0 )


def main():
    """ Generate collection of numbers """

    # Try each of these with large numbers for range().

    for z in get_numbers():
        print(z)

    for z in generate_numbers():
        print(z)

    for z in generate_numbers2():
        print(z)


    # Alternative ways to use a generator function and access a lazy
    # list using the builtin next() function and combined with a while loop.
    gen = generate_numbers()
    while True:
        num = next(gen, -1)
        if num != -1:
            print(num)
        else:
            break

    # Alternatively, manually get the next() object...
    gen = generate_numbers()
    num1 = next(gen, False)
    num2 = next(gen, False)
    num3 = next(gen, False)

    print(num1, num2, num3)
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)
