import time


def triangular(n):
    if n < 1:
        return None  # handle invalid input
    else:
        result = 0
        for i in range(1, n+1):
            result += i
        return result

def do_triangular(n):
    triangular_nums = []
    for i in range(1, n+1):
        triangular_nums.append(triangular(i))
    return triangular_nums


def test_last_parts():
    print("\nTEST:")
    CHECK_VALUES = ["25", "50", "00"]

    for i in range(1, 500+1):
            if i % 10 == 0: 
                triangular_number = str(triangular(i))
                if len(triangular_number) > 3 and triangular_number[-2:] in CHECK_VALUES:
                    print(f"{i}: ", triangular_number)
                

def remainder_by_x(number, x):
    return number % x

def rest_of_all(triangular_numbers):
    X = 3
    total = sum([remainder_by_x(value, X) for value in triangular_numbers])
    return total

def length(numbers):
    i = 0
    for number in numbers:
        if len(str(number)) > i:
            i = len(str(number))
    return i

def format_print(TRIANGULAR_NUMBERS, rests, bonuses):
    formatted_strings = ["", "", ""]
    for number, rest, bonus in zip(TRIANGULAR_NUMBERS, rests, bonuses):
        max_length = length([number, rest, bonus])
        formatted_strings[0] += "{0:>{1}}".format(number, max_length+2) + ","
        formatted_strings[1] += "{0:>{1}}".format(rest, max_length+2) + ","
        bonus_str = "{:+}".format(bonus)
        formatted_strings[2] += "{0:>{1}}".format(bonus_str, max_length+2) + ","
    
    i = 0
    while i < len(formatted_strings[0]):
        print(formatted_strings[0][i:i+170])
        print(formatted_strings[1][i:i+170])
        print(formatted_strings[2][i:i+170])
        print()
        i += 170


def test(range):
    rest_collection = []
    bonus = []
    current_length = 0
    TRIANGULAR_NUMBERS = do_triangular(range)
    while current_length < len(TRIANGULAR_NUMBERS):
        rest = rest_of_all(TRIANGULAR_NUMBERS[:current_length])
        rest_collection.append(rest)
        fake_num = TRIANGULAR_NUMBERS[current_length]+rest
        try:
            bonus.append(TRIANGULAR_NUMBERS[current_length+1]-fake_num)
        except:
            return (TRIANGULAR_NUMBERS, rest_collection, bonus)
        current_length += 1
    return (TRIANGULAR_NUMBERS, rest_collection, bonus)

if __name__ == "__main__":
    #(triangular_numbers, rest_collection, bonus) = test(98)
    #format_print(triangular_numbers, rest_collection, bonus)

    start_time = time.perf_counter_ns()
    do_triangular(98)
    end_time = time.perf_counter_ns()
    print(f"time: {end_time - start_time}")