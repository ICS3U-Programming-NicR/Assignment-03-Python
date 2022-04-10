#!/usr/bin/env python3

# Created By: Nicolas Riscalas

# Date: 08-04-2022

# Figures out what quality are the characters


def try_again_fnct():
    try_again = str(input("Would you like to try again? \n"))
    if try_again == "Y" or try_again == "y" or try_again == "yes" or try_again == "YES":
        main()
    elif try_again == "N" or try_again == "n" or try_again == "no" or try_again == "NO":
        print("Thanks for playing!")
        input("If you want to play again just press <enter>")

def main():
    counter = 0
    user_string = input(
        "Enter a string of characters, special operators(you can also include punctuation). "
    )
    for index, letter in enumerate(user_string):
        try:
            user_string_int = int(user_string[index])
            print(
                "The {} character ({}) is a number".format(index + 1, user_string_int)
            )
            counter += 1
        except:
            print(
                "The {} character ({}) is ".format(index + 1, user_string[index]),
                end="",
            )
            if letter in "aeiouAEIOU":
                print("vowel")
                counter += 1
            elif letter in "PTRWQSDFGHJKLZXCVBNMptrwqsdfghjklzxcvbnm":
                print("a consonant")
                counter += 1
            elif letter == " ":
                print("a space")
                counter += 1
            elif letter in "yY":
                print("both a vowel and consonant")
                counter += 1
            elif letter in ",.?:;!" + '"' + "'":
                print("a type of punctuation")
                counter += 1
            else:
                print("a special character")
                counter += 1
        if counter == len(user_string):
            try_again_fnct()
        

if __name__ == "__main__":
    main()
