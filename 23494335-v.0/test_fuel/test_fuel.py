from fuel import convert, gauge
import pytest

def test_convert_non_number():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("cat/1")
    with pytest.raises(ValueError):
        convert("1/dog")
    with pytest.raises(ValueError):
        convert("1.0/1")
    with pytest.raises(ValueError):
        convert("1/1.0")
    assert(convert("1/2") == 50)

def test_convert_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("2/1")

def test_convert_y_is_0():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert(gauge(100) == "F")
    assert(gauge(99) == "F")
    assert(gauge(0) == "E")
    assert(gauge(1) == "E")
    assert(gauge(50) == "50%")
