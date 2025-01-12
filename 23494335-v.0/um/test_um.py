from um import count

def test_default():
    assert(count("hello, um, world") == 1)

def test_part_of_world():
    assert(count("tummy") == 0)

def test_beginning_of_input():
    assert(count("um hello, um, world") == 2)

def test_end_of_input():
    assert(count("hello, um, world um.") == 2)

def test_case_insensitive():
    assert(count("hello, Um, world") == 1)
