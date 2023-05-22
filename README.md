### Simple bonus/remainder finder code block:
```py
X = 3
TARGET_VALUE = 28 # Next triangle number 
CURRENT_PRIMES = [0, 1, 3, 6, 10, 15, 21] # All previous triangle numbers
remainder = sum(CURRENT_PRIMES)%3 # Remainder formula
bonus = TARGET_VALUE - (CURRENT_PRIMES[-1] + remainder) # Bonus formula
print(f"target value: {TARGET_VALUE}")
print(f"remainder: {remainder}")
print(f"bonus: {bonus}")
print(f"next triangle number: {CURRENT_PRIMES[-1] + remainder + bonus}") # Verification 
```

### Simple grid with triangle numbers, remainders and bonuses
```
1, 3, 6, 10, 15, 21, 28, # Triangle numbers
-, -, -, --, --, --, --, 
0, 1, 1,  1,  2,  2,  2, # Remainders
1, 1, 2,  3,  3,  4,  5, # Bonuses
```