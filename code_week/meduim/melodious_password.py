#https://www.hackerrank.com/contests/w30/challenges/melodious-password/

import sys
from itertools import product, zip_longest
from string import ascii_lowercase

vowel = "bcdfghjklmnpqrstvwxz"
consonant = "aeiou"

number = int(input())
number_vowel = 0
number_consonat = 0
if number % 2 == 0:
    number_vowel = int(number / 2)
    number_consonat = int(number / 2)
else:
    number_vowel = int(number / 2) + 1
    number_consonat = int(number / 2)


def all_permutation_with_length(the_set, length):
    return [''.join(i) for i in product(the_set, repeat=length)]


part_of_vowel = all_permutation_with_length(vowel, number_vowel)
part_of_consonant = all_permutation_with_length(consonant, number_consonat)


def zipNfilter(only_vowels, only_consonants):

    ### list$ of pair that contain the valid permutation
    zipped_list = list(zip_longest(only_vowels, only_consonants))

    return ("".join(([
        element for tupl in zipped_list for element in tupl if element != None
    ])))


def filterrr(word, consonant, vowel):
    if set(word[::2]) <= set(consonant) and set(word[1::2]) <= set(vowel):
        return True
    elif set(word[1::2]) <= set(consonant) and set(word[0::2]) <= set(vowel):
        return True
    else:
        return False


for only_vowels in part_of_vowel:
    for only_consonants in part_of_consonant:

        ###  Vowel Consonant Vowel Consonant
        print(zipNfilter(only_vowels, only_consonants))
        if number % 2 == 0:
            ###  Consonant Vowel Consonant Vowel
            print(zipNfilter(only_consonants, only_vowels))

if number % 2 != 0:
    number_vowel, number_consonat = number_consonat, number_vowel

    part_of_vowel = all_permutation_with_length(vowel, number_vowel)
    part_of_consonant = all_permutation_with_length(consonant, number_consonat)

    for only_vowels in part_of_vowel:
        for only_consonants in part_of_consonant:
            print(zipNfilter(only_consonants, only_vowels))
