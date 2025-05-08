#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):  # check if the char is lower
            print(chr(ord(char) - 32), end='')  # convert to upper ASCII
        else:
            print(char, end='')  # print the char as is if it's not a lower
    print()  # print a new line at the end
