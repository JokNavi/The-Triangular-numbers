import BruteForce_clone as BruteForceClone
import generate_remainder_2 as GenerateRemainder2

def length(numbers):
    return max(len(str(number)) for number in numbers)

def format_print(TRIANGULAR_NUMBERS, rests, bonuses):
    formatted_strings = ["", "", ""]
    for number, rest, bonus in zip(TRIANGULAR_NUMBERS, rests, bonuses):
        max_length = length([number, rest, bonus])
        formatted_strings[0] += f"{number:>{max_length+2}}" + ","
        formatted_strings[1] += f"{rest:>{max_length+2}}" + ","
        formatted_strings[2] += f"{bonus:>{max_length+2}}" + ","
    i = 0
    while i < len(formatted_strings[0]):
        print(formatted_strings[0][i:i+170])
        print(formatted_strings[1][i:i+170])
        print(formatted_strings[2][i:i+170])
        print()
        i += 170


def run_brute_force():
    (triangular_numbers, rest_collection, bonus) = BruteForceClone.test(98)
    format_print(triangular_numbers, rest_collection, bonus)

def run_remainder_2():
    sum_remainders = GenerateRemainder2.generate_sum_remainder(150)
    bonuses = GenerateRemainder2.generate_bonus(150)
    triangular_row = GenerateRemainder2.generate_triangular_row(sum_remainders, bonuses)
    format_print(triangular_row, sum_remainders, bonuses)

if __name__ == "__main__":
    print("BRUTE FORCE CLONE: ")
    run_brute_force()
    print("REMAINDER 2: ")
    run_remainder_2()
