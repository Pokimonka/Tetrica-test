import pytest

from Task1.solution import sum_two, all_types


def test_sum_func():
    arg1 = 5
    arg2 = 7
    result = 12
    check = sum_two(arg1, arg2)
    assert check == result

@pytest.mark.parametrize(
    'arg1, arg2',
    (
            ('4', 'y'),
            ('pat', True),
            ([8,9], 9)

    )
)
def test_raise_sum_func(arg1, arg2):
    with pytest.raises(TypeError):
        sum_two(arg1, arg2)


def test_all_types_func():
    arg1 = 'Helen'
    arg2 = 21
    arg3 = 55.5
    arg4 = True
    arg5 = [1, 5, 11, 'viu-viu']
    result = "Helen2155.5True[1, 5, 11, 'viu-viu']"
    check = all_types(arg1, arg2, arg3, arg4, arg5)
    assert check == result

@pytest.mark.parametrize(
    'arg1, arg2, arg3, arg4, arg5',
    (
            ('4', 'y', '', '55', 43),
            (True, 55.7, False, '55', ['k', 't']),
            ('i', 22, 45.77, False, {'p':56})

    )
)
def test_raise_all_types_func(arg1, arg2, arg3, arg4, arg5):
    with pytest.raises(TypeError):
        all_types(arg1, arg2, arg3, arg4, arg5)