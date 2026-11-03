import Lab2

def test_find_min_max():
    result = []
    input_arr = [5, 67, 32]
    test_arr = [5, 67]

    result = Lab2.find_min_max(input_arr)
    assert(result == test_arr)

def test_calc_average():
    result = 0
    input_arr = [4, 5, 6]
    test_arr = 5

    result = Lab2.calc_average(input_arr)
    assert(result == test_arr)

def test_calc_median_temperature():
    result = 0
    input_arr = [5, 67, 32]
    test_arr = 32

    result = Lab2.calc_median_temperature(input_arr)
    assert(result == test_arr)
    