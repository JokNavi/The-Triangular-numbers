def get_bonus_x(remainder, triangle_seq, i ):
    return triangle_seq[i+1] - (remainder + triangle_seq[i])

def get_bonus_range(remainder_seq, triangle_seq):
    return [get_bonus_x(remainder, triangle_seq, i) for i, remainder  in enumerate(remainder_seq[:-1])]