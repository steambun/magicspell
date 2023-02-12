import random

def generate_word_list(filepath,validation_function):
    word_file=open(filepath,encoding='UTF-8')

    # create a word list
    word_list=[]

    # create list of valid words
    for dirty_word in word_file:
        word=dirty_word.strip()
        if validation_function(word):
            word_list.append(word)
    return word_list

def is_valid_random_word (guess):
    return (len(guess) ==7 and
        guess.find("'") ==-1 and
        not guess[0].isupper() and
        not word_has_duplicate_letters(guess))

def is_valid_subset_word(guess):
    return (len(guess) >=4 and
        guess.find("'") ==-1 and
        not guess[0].isupper())

def word_has_duplicate_letters(word):
    word_no_duplicates=set(word)
    return len(word_no_duplicates)!=len(word)

def generate_random_word_list(filepath):
    return generate_word_list(filepath,is_valid_random_word)

def generate_subset_word_list(filepath):
    return generate_word_list(filepath,is_valid_subset_word)

def generate_random_word():
    word_list=generate_word_list("wordlist.txt",is_valid_random_word)
    list_length = len(word_list)
    word = word_list[random.randint(0,list_length-1)]
    return word

def generate_random_letter_order():
    random_list = random.sample(range(7),7)
    return random_list

def find_valid_subset_words(filepath,input_word):
    word_list = generate_subset_word_list(filepath)
    subset_word_list=[]

    for word in word_list:
        if(set(word).issubset(input_word)):
            subset_word_list.append(word)

    return subset_word_list
