## For all triangle numbers: 

`TRIANGLE_NUMBERS[i] == CURRENT_PRIMES[i-1] + remainder + bonus`
```py
X = 3
TARGET_VALUE = 21 # Next triangle number 
TRIANGLE_NUMBERS = [0, 1, 3, 6, 10, 15] # All previous triangle numbers
remainder = sum(TRIANGLE_NUMBERS)%X # Remainder formula
bonus = TARGET_VALUE - (TRIANGLE_NUMBERS[-1] + remainder) # Bonus formula
print(f"target value: {TARGET_VALUE}")
print(f"remainder: {remainder}")
print(f"bonus: {bonus}")
print(f"next triangle number: {TRIANGLE_NUMBERS[-1] + remainder + bonus}") # Verification 
```

### Example grid.
```
1,  3,  6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91,105, # Triangle numbers
-,  -,  -, --, --, --, --, --, --, --, --, --, --,---,
0,  1,  1,  1,  2,  2,  2,  3,  3,  3,  4,  4,  4,  5, # Remainders
1,  1,  2,  3,  3,  4,  5,  5,  6,  7,  7,  8,  9,  9, # Bonuses
```


## For all Remainders:
`Remainders[i] == round(i/X)`

## For all Bonuses:
`Bonuses[i] == 2*i//X+1`
