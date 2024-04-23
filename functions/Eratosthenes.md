# Sieve of Eratosthenes
1. make a list of the numbers 2 up to your maximum desired prime
2. start with first entry in the list (2), and remove all multiples of it (4, 6, 8, 10, etc.)
3. go to next entry (3), and remove all multiples of it (6, 9, 12, etc.)
   * note that you will "remove" some numbers already removed by a previous multiple (e.g., 6 is a multiple of 2 and 3)
4. when you're done, all numbers that are left are prime

* 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
* 2 3 ~~4~~ 5 ~~6~~ 7 ~~8~~ 9 ~~10~~ 11 ~~12~~ 13 ~~14~~ 15 ~~16~~ 17 ~~18~~ 19 ~~20~~ 21 ~~22~~ 23 ~~24~~ 25
* 2 3 ~~4~~ 5 ~~6~~ 7 ~~8~~ ~~9~~ ~~10~~ 11 ~~12~~ 13 ~~14~~ ~~15~~ ~~16~~ 17 ~~18~~ 19 ~~20~~ ~~21~~ ~~22~~ 23 ~~24~~ 25
* 2 3 ~~4~~ 5 ~~6~~ 7 ~~8~~ ~~9~~ ~~10~~ 11 ~~12~~ 13 ~~14~~ ~~15~~ ~~16~~ 17 ~~18~~ 19 ~~20~~ ~~21~~ ~~22~~ 23 ~~24~~ ~~25~~
