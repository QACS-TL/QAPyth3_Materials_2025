#! /bin/python
# Name:        demo_collections_copying.py
# Author:      QA2.0, Donald Cameron
# Revision:    v1.0
# Description: This program will demonstrate how to copy collections
# by memory reference, shallow copy and deep copy.
"""
    Copying 2_Collections.
"""
import sys
import pprint
import copy

def main():
    """ Copy 2_Collections """
    movies = { 'Donald': ['Dracula', 'Deliverance', 'Descendants'],
               'Mira': ['Matrix', 'Mad Max', 'Magnolia'],
               'Sarah': ['Seven', 'Scream', 'Saving Private Ryan']
    }


    # Comment each of the following one at a time!
    films = movies # Copy by memory reference
    # films = movies.copy() # Shallow Copy, nested objects shared.
    # films = copy.deepcopy(movies) # Deep copy to all levels.

    movies['Mira'][1] = 'Magnificent Seven'
    movies['Brian'] = ['Braveheart', 'Brave', 'Babe']

    pprint.pprint(movies)
    print("-" * 60)
    pprint.pprint(films)

    films = movies
    pprint.pprint(films)

    favenums = { 'Donald': 34, 'Mira': 56, 'Sarah': 99 }

    # **********************************

    # weather = {'Glasgow': 11,
    #            'London': 21,
    #            'Edinburgh': 15,
    #            'Manchester': 18,
    #            'Thurso': 9
    #            }
    #
    # temps = weather.copy()
    # weather['London'] = 55
    # print(weather)
    # print(temps)
    #
    # list = ['Banana', 'Apple', 'Pear']
    # fruit = list.copy()
    # list[1] = 'Orange'
    #
    # print(list)
    # print(fruit)
    #
    # list = [['Banana', 'Yellow'], ['Apple', 'Red'], ['Pear', 'Green']]
    # fruit = list.copy()
    # list[1][0] = 'Orange'
    #
    # print(list)
    # print(fruit)
    #
    # list = [55, 66, 77]
    # nums = list.copy()
    # list[1] = list[1] + 22
    #
    # print(list)
    # print(nums)

    return None

if __name__ == "__main__":
    main()
    sys.exit(0)
