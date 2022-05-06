import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 6, 10, 44]
    test_arr = [6, 10, 11, 12, 22, 25, 34, 44, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)


def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 6, 10, 44]
    test_arr = [90, 64, 44, 34, 25, 22, 12, 11, 10, 6]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)


def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 6, 10, 44]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])


def test_bubble_sort_lesser():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 6, 10]
    test_n = 2
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_n)


def test_bubble_sort_more():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 6, 10, 44, 55]
    test_n = 1
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_n)


def test_bubble_sort_no():
    input_arr = []
    test_n = 0
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_n)


def test_bubble_sort_number():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 6, 10, 'e']
    test_n = 3
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_n)


