# Do this work in a new file, ***words.py***.

# 1. For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!
# 2. Turn that into a function, ***print_upper_words***. Test it out. (Don’t forget to add a docstring to your function!)
# 3. Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).
# 4. Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.
    
#     For example:
# this should print "HELLO", "HEY", "YO", and "YES"

# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
#                    must_start_with={"h", "y"})


# 1 - 2

def print_upper_words (words):
    ''' Print each word seperate line and uppercased'''
    for word in words:
        print(word.upper())


# 3
             
    def print_upper_words2(words):
        ''' Print each word seperate line, uppercased and starts with "E" '''
        for word in words:
            if word.startswith("e") or word.startswith("E"):
                print(word.upper())



# 4

    def print_upper_words3 (words, start_with) :

        ''' Print each word seperate line, uppercased and starts with one of given letters'''
        for word in words:
            for letter in start_with:
                if word.startswith(letter):
                    print(word.upper())
                    break                            