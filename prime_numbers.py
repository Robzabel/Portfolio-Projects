"""To check if a number is prime you need to establish if the numbers beneth it are divisible. 
2 is a prime number because it is divisible by itself and the only other number beneth it is 1; ergo, a prime number.
3 only has 1 and 2 below it, we can easily work out that 3 is not divisible by 2 so the only other number is 1 which makes it prime.
4 is divisible by 2 so its not prime, and so on"""

for n in range(2, 10):                                     # Create a loop through the range of numbers we want to check are prime or not
    for x in range(2,n):                                   # Create a loop that goes up to the value of the number we are checking so that we can iterate over the numbers below it
        if n % x == 0:                                     # This compares the nubers below the number being tested to see if they leave a remainder, if they do then they ar prime, if they == 0, they are not prime
            print(f"{n} equals {x} * {n//x}")              # This explains the situation
            break                                          # We then break out of the for loop
    else:                                                  # by using this else, it means that all the code ran to completion and no breaks, continues or errors were encountered 
            print(f"{n} is a prime number!")               # This is printed if the number is prime because the nested if statement is never entred