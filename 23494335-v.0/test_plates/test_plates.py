from plates import is_valid

def test_at_least_two_letter_begin():
    assert(is_valid("cs50"))
    assert(not is_valid("50cs"))
    assert(not is_valid("c50"))

def test_max_6_chars():
    assert(is_valid("cscs50"))
    assert(not is_valid("cscs501"))

def test_numbers_in_the_middle():
    assert(is_valid("cscs50"))
    assert(not is_valid("cs50cs"))

def test_number_not_begin_with_0():
    assert(not is_valid("cs05"))

def test_no_punctuation():
    assert(not is_valid("i'msam"))
    assert(not is_valid("imsam,"))
    assert(not is_valid("imsam."))

def test_no_space():
    assert(not is_valid("i am q"))
