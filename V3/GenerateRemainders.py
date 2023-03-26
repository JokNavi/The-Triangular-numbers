def get_remainder_x(triangular_numbers, x, i):
    return sum([value % x for value in triangular_numbers[:i]])

def get_remainder_range(triangular_seq, x):
    return [get_remainder_x(triangular_seq, x, i) for i in range(0, len(triangular_seq))]

if __name__ == "__main__":
    pass