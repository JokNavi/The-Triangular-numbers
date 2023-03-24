import math
import time


def generate_sum_remainder(length):
    output = []
    for i in range(length):
        output.extend([i]*3)
    return output[2:math.floor(length/3)]

def generate_bonus(length):
    output = [1]
    for i in range(0, math.floor(length/3))[::3]:
        next_value = output[i]+1
        output.append(next_value)
        output.append(next_value)
        output.append(next_value+1)
    return output[1:]

def generate_triangular_row(sum_remainders, bonuses):
    output = [1]
    i = 0
    for remainder, bonus in zip(sum_remainders, bonuses):
        output.append(output[i] + remainder + bonus)
        i += 1
    return output



start_time = time.perf_counter_ns()
sum_remainders = generate_sum_remainder(875)
bonuses = generate_bonus(290)
print(generate_triangular_row(sum_remainders, bonuses))
end_time = time.perf_counter_ns()

print(f"time: {end_time - start_time}")

