from jar import Jar
import pytest

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_init():
    with pytest.raises(ValueError):
        jar = Jar(-1)

def test_overflow():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.deposit(13)

def test_withdraw_too_many():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(1)
