
import pytesе
from utils import arrs


@pytest.mark.parametrize("a, i, d, result", [([1, 2, 3], 1, "test", 2),
                                             ([1, 2, 3], 0, "test", 1),
                                             ([1, 2, 3], 2, "test", 3),
                                             ([], 0, "test", "test"),
                                             ([1, 2, 3], -1, "test", "test")])
def test_get(a, i, d, result):
    assert arrs.get(a, i, d) == result


@pytest.mark.parametrize("a, b, c, result", [([1, 2, 3, 4], 1, 3, [2, 3]),
                                             ([1, 2, 3, 4], 0, 3, [1, 2, 3]),
                                             ([], 0, 0, []),
                                             ([1, 2, 3], None, 3, [1, 2, 3])])
def test_slice(a, b, c, result):
    assert arrs.my_slice(a, b, c) == result


@pytest.mark.parametrize("a, b, result", [([1, 2, 3], 0, [1, 2, 3]),
                                          ([1, 2, 3], 1, [2, 3]),
                                          ([1, 2, 3], 2, [3]), ])
def test_slice_more(a, b, result):
    assert arrs.my_slice(a, b) == result



def test_with_error():
    with pytest.raises(TypeError):
        assert arrs.my_slice([1, 2, 3], "2") == [3]
        assert arrs.get([1, 2, "3"], 1, "test") == 2
