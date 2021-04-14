#A Programme to substitue multiples of 3 with the word Fizz and multiples of 5 with the word Buzz, if the number is a multiple of both, it will print Fizz Buzz

for i in range(1 , 101):                    # The for loop iterates over the 100 numbers
    if i in range (0, 101, 3):              # The first if statement checks if the number is a multiple of 3
        if i in range(0, 101, 5):           # The nested if checks if it is also a multiple of 5
            i = "Fizz Buzz"                 # If both criteria match, Fizz Buzz is printed
            print(i)        
        else:                               # If the number is not a multiple of 5, Fizz is printed
            i = "Fizz"
            print(i)
    elif i in range(0, 101, 5):             # This elif statement checks if the number is only a multiple of 5
        i = "Buzz"
        print(i)
    else:                                   # If neither of the if statements amatch the number, the number is printed
        print(i)



for n in range(1, 101):                     # This is the actual solution, it is much cleaner than mine.
    if n % 3 == 0 and n % 5 == 0:           # I couldnt remember how to word the modulus operator statements but i initially knew this is the preferred method.
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)