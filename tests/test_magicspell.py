from magicspell import is_valid_random_word,generate_random_word_list,word_has_duplicate_letters,find_valid_subset_words

def test_is_valid_random_word_safeword():
    assert is_valid_random_word("stiched")

def test_is_valid_random_word_uppercase():
    assert not is_valid_random_word("Rounder")

def test_is_valid_random_word_too_long():
    assert not is_valid_random_word("rounding")

def test_is_valid_random_word_too_short():
    assert not is_valid_random_word("round")

def test_is_valid_random_word_plural():
    assert not is_valid_random_word("there's")

def test_is_valid_random_word_duplicate_letters():
    assert not is_valid_random_word("summary")

def test_generate_random_word_list():
    word_list = generate_random_word_list("tests/test_wordlist.txt")
    assert 2==len(word_list)
    assert word_list[0]=="stiched"
    assert word_list[1]=="founder"

def test_word_has_duplicate_letters_1():
    assert word_has_duplicate_letters("dad")

def test_word_has_duplicate_letters_2():
    assert word_has_duplicate_letters("summary")

def test_word_has_no_duplicate_letters_1():
    assert not word_has_duplicate_letters("pot")

def test_word_has_no_duplicate_letters_2():
    assert not word_has_duplicate_letters("bacon")

def test_find_valid_subset_words():
    word_list = find_valid_subset_words("tests/test_subset_wordlist.txt","deborah")
    assert 3==len(word_list)
    assert word_list[0]=="board"
    assert word_list[1]=="robe"
    assert word_list[2]=="bored"
    