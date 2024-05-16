def maximun(first_value, second_value):
    return max(first_value, second_value)

def compare(first_value, second_value):
    if first_value > second_value:
        return 1
    if second_value > first_value:
        return -1
    return 0


def test_max_compare(first_value, second_value):
    return compare(first_value, second_value), maximun(first_value, second_value)

def main():
    pass
    print(test_max_compare(1, 15))
    print(test_max_compare(1, 45))
    print(test_max_compare(45, 2))


main()