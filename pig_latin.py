"""
Created on Thu Nov 14 10:14:24 2019

@author: 12kbe

Generator excepts a phrase and translates into pig latin
"""


def main():
    """Used to check if __main__"""
    phrase = input('Enter a phrase: ')
    vowels = ['a', 'e', 'i', 'o', 'u']

    phrase_list = phrase.split()
    pl_phrase = []

    for word in phrase_list:
        if word[0] in vowels:
            pl_phrase.append(word + 'way')
        else:
            pl_phrase.append(word[1:] + word[0] + 'ay')

    pl_phrase = " ".join(pl_phrase)

    print(pl_phrase)

if __name__ == "__main__":
    main()
