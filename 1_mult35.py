#! python3
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these
# multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

import logging

logging.basicConfig(level=logging.CRITICAL, format=' %(asctime)s - %(levelname)s- %(message)s')

# Upper bound for multiple search
upper = 1000

# Initialize sum
sum = 0

for i in range(1, upper):
    if i % 3 == 0:
        logging.debug("%d is a multiple of 3" % i)
        sum += i
    else:
        if i % 5 == 0:
            logging.debug("%d is a multiple of 5" % i)
            sum += i
    logging.debug("Huidige som: %d" % sum)

# Result
print("The sum of all natural numbers below %d that are multiples of 3 or 5 is %d" % (upper, sum))
wait = input("Press enter")
