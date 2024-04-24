# Sieve of Eratosthenes
* write a program to find prime numbers (numbers which are divisible only by themselves and 1, e.g., __`2, 3, 29, 31, 101, 419, 997`__) up to a given number using Eratosthene's Sieve:
  * start with a list of all of the numbers from 2 up to the given number, e.g., if the given number if 25, you'd start with

> __`[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]`__
  * remove all of the multiples of the first number (2), so you now have 

> __`[2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]`__
  * now remove all of the multiples of the next number (3), so you now have 

> __`[2, 3, 5, 7, 11, 13, 17, 19, 23, 25]`__
  * keep doing this, removing multiples of the next number (5), (i.e., 10, 15, 20, and 25–they're already all removed except for 25)
  * stop when 2 times the next number you land on is larger than the given number–in this case you'd stop at 13, since 13 * 2  > 25
  * at this point every number in the list is prime
  * try your solution with large numbers and compare against list of primes (e.g., https://miniwebtool.com/list-of-prime-numbers/)
  * removing the multiples from the list is fairly inefficient, and you should notice your program slowing down considerably with large numbers, so now try setting the multiples to 0, rather than removing them, e.g.,
    * __`[2, 3, 0, 5, 0, 7, 0, 9, 0, 11, 0, 13, 0, 15, 0, 17, 0, 19, 0, 21, 0, 23, 0, 25]`__
    * __`[2, 3, 0, 5, 0, 7, 0, 0, 0, 11, 0, 13, 0, 0, 0, 17, 0, 19, 0, 0, 0, 23, 0, 25]`__
    * __`[2, 3, 0, 5, 0, 7, 0, 0, 0, 11, 0, 13, 0, 0, 0, 17, 0, 19, 0, 0, 0, 23, 0, 0]`__

* once you've got it working, consider using a __`set`__ instead of a __`list`__
  * what changes?
  * which ones is more efficient?
