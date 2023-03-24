import time
import BruteForce
import generate_remainder_3 as GenRem3


def brute_force_speed():
    start_time = time.perf_counter_ns()
    for _ in range(0, 100):
        BruteForce.do_triangular(98)
        end_time = time.perf_counter_ns()
    return end_time - start_time

def generate_remainder_3_speed():
    start_time = time.perf_counter_ns()
    for _ in range(0, 100):
        sum_remainders = GenRem3.generate_sum_remainder(875)
        bonuses = GenRem3.generate_bonus(290)
        GenRem3.generate_triangular_row(sum_remainders, bonuses)
    end_time = time.perf_counter_ns()

    return end_time - start_time

def brute_force_speed_single(x):
    start_time = time.perf_counter_ns()
    BruteForce.do_triangular(196 * x)
    end_time = time.perf_counter_ns()
    return end_time - start_time

def generate_remainder_3_speed_single(x):
    start_time = time.perf_counter_ns()
    sum_remainders = GenRem3.generate_sum_remainder(1750 * x)
    bonuses = GenRem3.generate_bonus(580 * x)
    GenRem3.generate_triangular_row(sum_remainders, bonuses)
    end_time = time.perf_counter_ns()

    return end_time - start_time


if __name__ == "__main__":
    brute_force_speed_time = brute_force_speed_single(2)
    gen_rem_3_speed_time = generate_remainder_3_speed_single(2)
    print(f"brute_force_speed time: {brute_force_speed_time}")
    print(f"gen_rem_3_speed time: {gen_rem_3_speed_time }")
