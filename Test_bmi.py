import Lab2.bmi as bmi

print("Test Bmi")
def test_bmi_normal_weight():
    result = []
    height = 1.73
    weight = 57
    result = bmi.calculate_bmi(height, weight)
    assert (result == 0)


def test_bmi_over_weight():
    result = []
    height = 1.6
    weight = 80
    result = bmi.calculate_bmi(height, weight)
    assert (result == 1)


def test_bmi_under_weight():
    result = []
    height = 1.8
    weight = 50
    result = bmi.calculate_bmi(height, weight)
    assert (result == -1)
