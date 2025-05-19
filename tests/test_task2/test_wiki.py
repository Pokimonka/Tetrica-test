import pytest

from Task2.solution import parse


def test_parse_first_page():
    arg1 = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    result = ['А', '/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%90%D0%B7%D0%B8%D0%B0%D1%82%D1%81%D0%BA%D0%B8%D0%B5+%D1%82%D0%BE%D0%BA%D0%B8#mw-pages']
    check = parse(arg1)
    assert check == result

def test_parse_tenth_page():
    arg1 = "https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%91%D0%B5%D0%BB%D0%BE%D0%BB%D0%B8%D1%86%D0%B0%D1%8F+%D1%81%D0%BE%D0%B2%D0%BA%D0%B0#mw-pages"
    result = ['Б',
              '/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83&pagefrom=%D0%91%D0%B5%D0%BB%D1%8F%D0%BD%D0%BA%D0%B0+%D1%81%D1%82%D0%B5%D0%BF%D0%BD%D0%B0%D1%8F#mw-pages']
    check = parse(arg1)
    assert check == result

# @pytest.mark.parametrize(
#     'arg1, arg2',
#     (
#             ('4', 'y'),
#             ('pat', True),
#             ([8,9], 9)
#
#     )
# )
# def test_raise_sum_func(arg1, arg2):
#     with pytest.raises(TypeError):
#         sum_two(arg1, arg2)
#
#
# def test_all_types_func():
#     arg1 = 'Helen'
#     arg2 = 21
#     arg3 = 55.5
#     arg4 = True
#     arg5 = [1, 5, 11, 'viu-viu']
#     result = "Helen2155.5True[1, 5, 11, 'viu-viu']"
#     check = all_types(arg1, arg2, arg3, arg4, arg5)
#     assert check == result
#
# @pytest.mark.parametrize(
#     'arg1, arg2, arg3, arg4, arg5',
#     (
#             ('4', 'y', '', '55', 43),
#             (True, 55.7, False, '55', ['k', 't']),
#             ('i', 22, 45.77, False, {'p':56})
#
#     )
# )
# def test_raise_all_types_func(arg1, arg2, arg3, arg4, arg5):
#     with pytest.raises(TypeError):
#         all_types(arg1, arg2, arg3, arg4, arg5)