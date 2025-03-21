import pytest
from calculate import add,subtract,divide,multiply

def test_add():
    assert add(2,3)==5
    assert add(4,5)==9

def test_subtract():
    assert subtract(3,1)==2
    assert subtract(4,5)==-1

def test_multiply():
    assert multiply(2,3)==6
    assert multiply(4,5)==20

def test_divide():
    assert divide(27,3)==9
    assert divide(42,14)==3


