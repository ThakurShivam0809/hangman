import random
from words import words
import string

def valid_word(words):
    a = random.choice(words)
    while "_" in a or " " in a:
        a = random.choice(words)
    return a.upper()         

word = valid_word(words)
alphabets = set(string.ascii_uppercase) 
word_letter = set(word)
used_letter = set()
i = 5
while len(word_letter) > 0 :
    if i == 0:
        print("You ran out of attemps")
        break
    print(f"You have {i} lives left" )  
    print("You have used these leters: ", ' '.join(used_letter))
    progress_letters = [letter if letter in used_letter else '_' for letter in word ]
    print("The word so far is: ", ' '.join(progress_letters))
    user_input = input("Enter your Letter: ").upper()
    if user_input in alphabets - used_letter:
        used_letter.add(user_input)
        if user_input in word_letter:
            print("This is a correct letter. ")
            word_letter.remove(user_input)
        else :
            print("Incorrect!") 
            i = i-1    
    elif user_input in used_letter:
            print("You have already guessed that letter ")
    else:
        print("Invalid input") 
            
print(f"The word is: {word} ")