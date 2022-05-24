# What does this piece of code do?
# Answer: make the loop run 10 times and choose a number from (1,100) randomly and print out the last number

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

# set the initial value of "progress"
progress=0
# set the loop which can choose a random number in (1,100), after running 10 times, this loop stops.
while progress<10:
	progress+=1
	n = randint(1,100)

# output the value of n
print(n)
