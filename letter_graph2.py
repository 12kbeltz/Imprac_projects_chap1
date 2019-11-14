# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 10:45:00 2019

@author: 12kbe
"""
from pprint import pprint

def main():
    """Used to check for main"""
    phrase = input('Enter a phrase: ')
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter_dict = {}

    for letter in alphabet:
        letter_dict[letter] = []

    for letter in [i.lower() for i in phrase if i != " "]:
        letter_dict[letter].append(letter)

    pprint(letter_dict)

if __name__ == "__main__":
    main()
