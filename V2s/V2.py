import math

def generate_sum_remainder(length):
    output = []
    for i in range(length):
        output.extend([i]*3)
    return output

def generate_fast_bonus(length, sum_remainders):
    bonuses = []
    for i in range(0, length):
        bonuses.append(sum_remainders[i+1] + sum_remainders[i+2])
    return bonuses
    

def generate_triangular_row(sum_remainders, bonuses):
    output = [1]
    i = 0
    for remainder, bonus in zip(sum_remainders, bonuses):
        output.append(output[i] + remainder + bonus)
        i += 1
    return output   


if __name__ == "__main__":
    pass
