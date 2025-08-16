
import random

word_list=["camel","racoon","cat"]

# todo number 1 
choosen_word=random.choice(word_list)
print(choosen_word)

# todo number 2
guess=input("Guess the word").lower()
print(guess)

# todo number 3
for letter in choosen_word:
    if letter == guess:
        print("right")
    else:
        print("Wrong")    