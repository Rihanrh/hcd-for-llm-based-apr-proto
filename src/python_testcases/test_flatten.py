import pytest  # type: ignore
from python_programs.flatten import flatten

def test_flatten():
    assert list(flatten([[1, [], [2, 3]], [[4]], 5])) == [1, 2, 3, 4, 5]
    assert list(flatten([[], [], [], [], []])) == []
    assert list(flatten([[], [], 1, [], 1, [], []])) == [1, 1]
    assert list(flatten([1, 2, 3, [[4]]])) == [1, 2, 3, 4]
    assert list(flatten([1, 4, 6])) == [1, 4, 6]
    assert list(flatten(["moe", "curly", "larry"])) == ["moe", "curly", "larry"]
    assert list(flatten(["a", "b", ["c"], ["d"], [["e"]]])) == ["a", "b", "c", "d", "e"]