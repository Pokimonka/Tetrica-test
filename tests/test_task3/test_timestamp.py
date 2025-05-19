import pytest

from Task3.solution import appearance, make_pairs, take_all_intervals

tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

@pytest.mark.parametrize(
    'arg1, result',
    (
            (tests[0]['intervals'], 3117),
            (tests[1]['intervals'], 3577),
            (tests[2]['intervals'], 3565)

    )
)
def test_timestamp(arg1, result):
    check = appearance(arg1)
    assert check == result

@pytest.mark.parametrize(
    'list_for_pair, result',
    (
            ([1,2,3,4,5,6,7,8,9,0], [(1,2),(3,4),(5,6),(7,8),(9,0)]),
            ([65465,6565,6565,65454], [(65465,6565),(6565,65454)]),
            ([3,3,3,3,3,3,3,3,3,3], [(3,3),(3,3),(3,3),(3,3),(3,3)])

    )
)
def test_pairs(list_for_pair, result):
    check = make_pairs(list_for_pair)
    assert check == result

@pytest.mark.parametrize(
    'intervals, result',
    (
            ([1, 5, 3, 7, 8, 10], {1, 2, 3, 4, 5, 6, 8, 9}),
            ([45, 50, 20, 32], {45, 46, 47, 48, 49, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31}),
            ([3, 7, 2, 4], {2, 3, 4, 5, 6})

    )
)
def test_intervals(intervals, result):
    check = take_all_intervals(intervals)
    assert check == result
