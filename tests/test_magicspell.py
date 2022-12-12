from magicspell import is_valid_word,generate_word_list

def test_is_valid_word_safeword():
    assert is_valid_word("rounder")

def test_is_valid_world_uppercase():
    assert not is_valid_word("Rounder")

def test_is_valid_world_too_long():
    assert not is_valid_word("rounding")

def test_is_valid_world_too_short():
    assert not is_valid_word("round")

def test_is_valid_world_plural():
    assert not is_valid_word("there's")

def test_generate_world_list():
    word_list = generate_word_list("tests/test_wordlist.txt")
    assert 2==len(word_list)
    assert word_list[0]=="rounded"
    assert word_list[1]=="founder"
