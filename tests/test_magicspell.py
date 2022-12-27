from magicspell import is_valid_word,generate_word_list,word_has_duplicate_letters

def test_is_valid_word_safeword():
    assert is_valid_word("stiched")

def test_is_valid_word_uppercase():
    assert not is_valid_word("Rounder")

def test_is_valid_word_too_long():
    assert not is_valid_word("rounding")

def test_is_valid_word_too_short():
    assert not is_valid_word("round")

def test_is_valid_word_plural():
    assert not is_valid_word("there's")

def test_is_valid_word_duplicate_letters():
    assert not is_valid_word("summary")

def test_generate_word_list():
    word_list = generate_word_list("tests/test_wordlist.txt")
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
