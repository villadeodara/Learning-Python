from bank import value

def test_hello():
    assert(value("hello") == 0)

def test_hello_case_insenstive():
    assert(value("Hello, World!") == 0)

def test_begin_with_h():
    assert(value("hello") != 20)
    assert(value("hi") == 20)
    assert(value("Hey") == 20)

def test_not_begin_with_h():
    assert(value("what's up?") == 100)

def test_leading_white_space():
    assert(value("  hello") == 0)
    assert(value("  Hey") == 20)
    assert(value("  What's up") == 100)
