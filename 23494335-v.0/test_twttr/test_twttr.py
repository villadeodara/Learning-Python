from twttr import shorten

def test_default():
    assert(shorten("twitter") == "twttr")

def test_no_vower():
    assert(shorten("twttr") == "twttr")

def test_case_insensitive():
    assert(shorten("TWITTER") == "TWTTR")

def test_number():
    assert(shorten("1") == "1")

def test_punctuation():
    assert(shorten("Hello, World!") == "Hll, Wrld!")
