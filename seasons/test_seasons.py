from seasons import get_date
import pytest

def test_default():
    assert(get_date("1999-01-01") == (1999, 1, 1))

# As long as the format is correct, the tuple is returned. The invalid values
# for year, month, or day will be left for the date class to catch.
def test_right_format():
    assert(get_date("1999-13-34") == (1999, 13, 34))

def test_wrong_format():
    with pytest.raises(ValueError):
        get_date("cat")
