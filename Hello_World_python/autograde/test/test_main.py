import sys
import pytest
from .. import main

def test_hello_world():
    expected = 'Hello World'
    actual = main.hello_world()
    assert expected == actual

def test_hello_python():
    expected = 'Hello Python'
    actual = main.hello_python()
    assert expected == actual