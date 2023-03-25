## File 1: `triangular_numbers.py`
This file calculates triangular numbers, their remainders, and bonuses.

### Functions

1. `triangular(n: int) -> int:`

    Calculates the n-th triangular number.
    * Input: n (int) - The position of the desired triangular number.
    * Output: The n-th triangular number if n is greater than 0, otherwise returns None.

2. `do_triangular(n: int) -> List[int]:`

    Generates a list of the first n triangular numbers.

    * Input: n (int) - The number of triangular numbers to generate.
    * Output: A list of the first n triangular numbers.

3. `remainder_by_x(number: int, x: int) -> int:`

    Calculates the remainder of a given number when divided by x.

    * Input: number (int) - The number to calculate the remainder for, x (int) - The divisor.
    * Output: The remainder of the division.

4. `rest_of_all(triangular_numbers: List[int]) -> int:`

    Calculates the sum of remainders when each triangular number is divided by 2.

    * Input: triangular_numbers (List[int]) - A list of triangular numbers.
    * Output: The sum of remainders.

5. `test(n: int) -> Tuple[List[int], List[int], List[int]]:`

    Generates triangular numbers, their rest collections, and bonuses for the first n numbers.

    * Input: n (int) - The number of triangular numbers to generate.
    * Output: A tuple containing the list of triangular numbers, the list of rest collections, and the list of bonuses.

---

## `File 2: generate_remainder_2.py`
This file generates the sum remainder, bonuses, and triangular row for a given length.

### Functions

1. `generate_sum_remainder(length: int) -> List[int]:`

    Generates a list of sum remainders for the given length.

    Input: length (int) - The length of the desired sum remainders.
    Output: A list of sum remainders.
2. `generate_bonus(length: int) -> List[int]:`

    Generates a list of bonuses for the given length.

    * Input: length (int) - The length of the desired bonuses.
    * Output: A list of bonuses.
3. `generate_triangular_row(sum_remainders: List[int], bonuses: List[int]) -> List[int]:`

    Generates a triangular row using the given sum remainders and bonuses.

    * Input: sum_remainders (List[int]) - A list of sum remainders, bonuses (List[int]) - A list of bonuses.
    * Output: A list representing the triangular row.

---

## `File 3: main.py`
This file imports and runs the functions from the other two files and formats the output.

### Functions

1. `length(numbers: List[int]) -> int:`

    Finds the maximum length (number of digits) of the given list of numbers.

    * Input: numbers (List[int]) - A list of numbers.
    * Output: The maximum length of the numbers in the list.
2. `format_print(TRIANGULAR_NUMBERS: List[int], rests: List[int], bonuses: List[int]) -> None:`

    Formats and prints the given lists of triangular numbers, rests, and bonuses in a structured manner.

    * Input: TRIANGULAR_NUMBERS (List[int]) - A list of triangular numbers, rests (List[int]) - A list of rests, bonuses (List[int]) - A list of bonuses.
    * Output: None. Prints the formatted output.
3. `run_brute_force() -> None:`

    Executes the brute force clone method, formats the output, and prints the results.

    * Input: None.
    * Output: None. Prints the formatted results.
4. `run_remainder_2() -> None:`

    Executes the remainder 2 method, formats the output, and prints the results.

    * Input: None.
    * Output: None. Prints the formatted results.

---
  
## `Usage`

    if __name__ == "__main__":
        print("BRUTE FORCE CLONE: ")
        run_brute_force()
        print("REMAINDER 2: ")
        run_remainder_2()

When this script is run, it will execute the run_brute_force and run_remainder_2 functions, which will print the formatted output for each method.

---

## `Generate_remainder_2`

The Generate_remainder_2.py file contains three functions that work together to generate a sequence of triangular numbers with specific properties. The mathematical formula that captures the essence of this file can be represented as follows:

`T_n = T_(n-1) + R_n + B_n`

### Where:
- T_n represents the nth triangular number in the sequence
- R_n represents the nth sum remainder
- R_n = 3 * floor(n/3) - 2 (for n >= 2)
- B_n represents the nth bonus
- B_n = 1 + floor(n/3)

### Explanation:

1. generate_sum_remainder(length): This function generates a list of sum remainders (R_n) for the given length. The formula for R_n is derived from the loop in the function, which repeats each number i three times.

2. generate_bonus(length): This function generates a list of bonuses (B_n) for the given length. The formula for B_n is derived from the loop in the function,  which creates a sequence of the form 1, 1, 2, 2, 2, 3, 3, 3, 4, ...

3. generate_triangular_row(sum_remainders, bonuses): This function generates the triangular row (T_n) using the given sum_remainders and bonuses. The formula for T_n is derived from the loop in the function, which calculates each element of the output list as the sum of the previous element, the corresponding sum_remainder, and bonus.