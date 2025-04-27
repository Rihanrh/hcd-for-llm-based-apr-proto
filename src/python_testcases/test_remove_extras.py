import pytest  # type: ignore
from python_programs.remove_extras import remove_extras

def test_remove_extras():
    assert remove_extras([1, 1, 1, 2, 3]) == [1, 2, 3]
    assert remove_extras([1, 5, 1, 1, 3, 2]) == [1, 5, 3, 2]
    assert remove_extras([]) == []
    assert remove_extras([3, 4, 5, 1, 3]) == [3, 4, 5, 1]