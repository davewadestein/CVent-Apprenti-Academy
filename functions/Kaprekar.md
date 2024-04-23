# Kaprekar's Routine
* given a 4-digit number where not all digits are the same that Kaprekar's Routine (described below) will always converge to Kaprekar's Constant (6174)
* algorithm:
  1. Take any four-digit number, using at least two different digits (leading zeros are allowed)
  1. Arrange the digits in descending and then in ascending order to get two four-digit numbers, adding leading zeros if necessary
  1. Subtract the smaller number from the bigger number
  1. Go back to step ii and repeat

  * e.g., starting with the number 8991:

>>>
        9981 – 1899 = 8082
        8820 – 0288 = 8532
        8532 – 2358 = 6174
        7641 – 1467 = 6174
