"""
File: anagram.py
Name: Rosy Huang
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO: This program recursively finds all the anagram(s)
for the word input by user.
    """
    print("Welcome to stanCode \"anagram generator\"(or -1 to quit)")
    while True:
        s = input("Find anagram for: ")
        start = time.time()
        if s == EXIT:
            break
        dict_list = read_dictionary()
        find_anagrams(s, dict_list)
        end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    with open(FILE, "r") as f:
        dict_list = []
        for line in f:
            dict_list.append(line.strip())
    return dict_list


def find_anagrams(s, dict_list):
    """
    :param s: input string s
    :param dict_list: list created by read_dictionary() which stores words from dictionary.txt
    :return:
    """
    store_new_s = []
    print("Searching...")
    find_anagram_helper(s, "", dict_list, [], store_new_s)
    print(len(store_new_s),"anagrams:", store_new_s)


def find_anagram_helper(s, new_s, dict_list, store_i, store_new_s):
    if len(new_s) == len(s):
        if new_s in store_new_s:  # new string is already printed
            pass
        elif new_s in dict_list:
            print("Found:",new_s)
            store_new_s.append(new_s)
            print("Searching...")
    else:
        for i in range(len(s)):
            if i in store_i:
                pass
            else:
                # Choose
                store_i.append(i)
                new_s += s[i]
                # Explore
                if has_prefix(new_s, dict_list) is True:
                    find_anagram_helper(s, new_s, dict_list, store_i, store_new_s)
                # Un-choose
                new_s = new_s[:len(new_s) - 1]
                store_i.pop()


def has_prefix(sub_s, dict_list):
    """
    :param sub_s: substring of new_s
    :param dict_list: list created by read_dictionary() which stores words from dictionary.txt
    :return:
    """
    for word in dict_list:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
