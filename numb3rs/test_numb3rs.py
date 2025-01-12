from numb3rs import validate

def test_default():
    assert(validate("1.2.3.4"))

def test_non_digits():
    assert(validate("cat") == False)

def test_multi_digits():
    assert(validate("127.0.0.1"))

def test_in_range():
    assert(validate("255.0.255.0"))
    assert(validate("255.255.255.255"))
    assert(validate("0.0.0.0"))

def test_out_of_range():
    assert(validate("275.2.3.1") == False)
    assert(validate("1.2000.3000.4000") == False)
    assert(validate("512.512.512.1000") == False)
