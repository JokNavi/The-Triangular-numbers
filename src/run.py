X = 9

def generate_remainders(amount: int):
    return [round(i/X) for i in range(1, amount+1)]

def generate_bonuses(amount: int):
    return [2*n//X+1 for n in range(0, amount)]

def generate_triangle_numbers(amount: int):
    remainders = generate_remainders(amount)
    bonuses = generate_bonuses(amount)
    last_triangle_number = 0
    return [(last_triangle_number := last_triangle_number + remainder + bonus) for remainder, bonus in zip(remainders, bonuses)]
    

if __name__ == "__main__":
    triangular_numbers = generate_triangle_numbers(100)
    remainders = generate_remainders(100)
    bonuses = generate_bonuses(100)

    for t, r ,b in zip(triangular_numbers, remainders, bonuses):
        print(f"+ {r} + {b} == {t}")

    print(generate_remainders(50))

