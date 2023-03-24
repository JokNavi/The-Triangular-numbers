def triangular(n):
    if n < 1:
        return None  # handle invalid input
    else:
        result = sum(range(1, n+1))
        return result


def do_triangular(n):
    return [triangular(i) for i in range(1, n+1)]


def remainder_by_x(number, x):
    return number % x


def rest_of_all(triangular_numbers):
    X = 2
    total = sum(remainder_by_x(value, X) for value in triangular_numbers)
    return total


def test(n):
    TRIANGULAR_NUMBERS = do_triangular(n)
    rest_collection = []
    bonus = []
    for i in range(n):
        rest = rest_of_all(TRIANGULAR_NUMBERS[:i])
        rest_collection.append(rest)
        fake_num = TRIANGULAR_NUMBERS[i] + rest
        try:
            bonus.append(TRIANGULAR_NUMBERS[i+1] - fake_num)
        except IndexError:
            return TRIANGULAR_NUMBERS, rest_collection, bonus


if __name__ == "__main__":
    triangular_numbers, rest_collection, bonus = test(98)
    # Print the results
    for lst in (triangular_numbers, rest_collection, bonus):
        print(", ".join(str(x) for x in lst))