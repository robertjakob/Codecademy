import scipy.stats as stats
import numpy as np

## Exercise 1
# sampling from a 6-sided die
die_6 = range(1, 7)
print(np.random.choice(die_6, size = 5, replace = True))


## Exercise 4 - binomial probability mass function
# 6 heads from 10 fair coin flips
print(stats.binom.pmf(6, 10, 0.5))


## Exercise 6 - binomial probability mass function
# 2 to 4 heads from 10 coin flips
# P(X = 2) + P(X = 3) + P(X = 4)
print(stats.binom.pmf(2, n=10, p=.5) + stats.binom.pmf(3, n=10, p=.5) + stats.binom.pmf(4, n=10, p=.5))

# 0 to 8 heads from 10 coin flips
# 1 - (P(X = 9) + P(X = 10))
print(1 - (stats.binom.pmf(9, n=10, p=.5) + stats.binom.pmf(10, n=10, p=.5)))


## Exercise 9 - binomial cumulative distribution function
# 6 or fewer heads from 10 coin flips
print(stats.binom.cdf(6, 10, 0.5))

# more than 6 heads from 10 coin flips
print(1 - stats.binom.cdf(6, 10, 0.5))

# between 4 and 8 heads from 10 coin flips
print(stats.binom.cdf(8, 10, 0.5) - stats.binom.cdf(3, 10, 0.5))


## Exercise 10 - normal distribution cumulative distribution function
# stats.norm.cdf(x, loc, scale)
# temperature being less than 14*C
  # x = 14, loc = 20, scale = 3
print(stats.norm.cdf(14, 20, 3))


# Exercise 11
# temperature being greater than 24*C
  # x = 24, loc = 20, scale = 3
print(1 - stats.norm.cdf(24, 20, 3))

# temperature being between 21*C and 25*C
  # x = 24, loc = 20, scale = 3
print(stats.norm.cdf(25, 20, 3) - stats.norm.cdf(21, 20, 3))


# Further Practice Quesions from MORE ON PROBABILITY DISTRIBUTIONS

# Practice Question 1: 
# You work at ambulance dispatch where the number of calls that come in daily follows the Poisson distribution with lambda equal to 9. There’s a rule that a team can go on no more than 12 calls a day. But how often could this happen?
# Create a variable calls that is the probability of observing more than 12 calls on a given day. Then print calls.
calls = 1 - stats.poisson.cdf(12, 9)
print(calls)

# Practice Question 2: 
# Let’s say that you have to call in a backup team if you have 10 or more calls in a given day. But you don’t want to have to call in a backup team unless they really will be needed. But what is the probability that they will be called and not needed?
# Create and print a variable false_backup that is the probability of observing a minimum of 10 calls, but no more than 12. Then print false_backup.
false_backup = stats.poisson.cdf(12, 9) - stats.poisson.cdf(9, 9)
print(false_backup)

# Practice Question 3: 
# A certain tennis star has a first-serve rate of 62%. Let’s say they serve 80 times in a given match. What is the expected value of the number of serves they make?
# Create and print a variable expected_serves that is the number of first-serves they are expected to make.
expected_serves = 80*0.62
print(expected_serves)

# Practice Question 4
# At the same first-serve rate, what is the variance of this player’s first-serves?
# Create and print a variable variance_serves that is the variance of the player making their first serve.
variance_serves = 80*0.62*(1-0.62)
print(variance_serves)
