import random

LENGTH_OF_WORD = 7

def is_valid_word (guess):
    return (len(guess) ==LENGTH_OF_WORD and
        guess.find("'") ==-1 and
        not guess[0].isupper() and
        not word_has_duplicate_letters(guess))

def word_has_duplicate_letters(word):
    word_no_duplicates=set(word)
    return len(word_no_duplicates)!=len(word)

def generate_word_list(filepath):
    word_file=open(filepath,encoding='UTF-8')

    # create a word list
    word_list=[]

    # create list of valid words
    for dirty_word in word_file:
        word=dirty_word.strip()
        if is_valid_word(word):
            word_list.append(word)
    return word_list

def generate_random_word():
    word_list=generate_word_list("wordlist.txt")
    list_length = len(word_list)
    word = word_list[random.randint(0,list_length-1)]
    print(word)
    return word

def generate_random_letter_order():
    random_list = random.sample(range(7),7)
    return random_list
