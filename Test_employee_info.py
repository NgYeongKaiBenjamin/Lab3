import employee_info

print("Employee info test")


def test_get_employees_by_age_range():
    result = []
    answer = [
        {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
        {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000}
    ]
    result = employee_info.get_employees_by_age_range(20, 30)
    assert (result == answer)


def test_calculate_average_salary():
    result = []
    answer = 60167
    result = employee_info.calculate_average_salary()
    assert (round(result) == answer)


def test_get_employees_by_dept():
    result = []
    answer = [
        {"name": "Chloe", "age": 35, "department": "Engineering", "salary": 70000},
        {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}
    ]
    result = employee_info.get_employees_by_dept("Engineering")
    assert (result == answer)
