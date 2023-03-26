import Formatting
import GenerateBonuses as GenBonuses
import GenerateRemainders as GenRemainders
import GenerateTriangleNumbers as GenTriangleNumbers

def run():
    LENGTH = 100
    triangle_seq = GenTriangleNumbers.get_triangle_range(LENGTH)
    remainder_seq = GenRemainders.get_remainder_range(triangle_seq, 3)
    bonus_seq = GenBonuses.get_bonus_range(remainder_seq, triangle_seq)
    display_list = [triangle_seq, remainder_seq, bonus_seq]
    separator = Formatting.get_seperator(display_list)
    display_list.insert(1, separator)
    Formatting.print_nicely(display_list)
        

if __name__ == "__main__":
    run()