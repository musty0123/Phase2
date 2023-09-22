import pytest
from lib.make_snippet import *

def test_empty_snippet():
    result = snip("")
    assert result == ""

def test_make_snippet():
    result = snip("the cat jumps over")
    assert result == "the cat jumps over"

def test_make_snippet_five():
    result = snip("the cat jumps over a fence")
    assert result == "the cat jumps over a ..."



