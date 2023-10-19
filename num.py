import random

upper_limit = input("Please enter the upper limit for the number range: ")
lower_limit = input("Please enter the lower limit for the number range: ")

if upper_limit.isdigit():
    upper_limit = int(upper_limit)
else:
    print("Enter a valid number for the next time")
    quit()

if lower_limit.isdigit():
    lower_limit = int(lower_limit)
else:
    print("Enter a valid number for the next time")
    quit()

if upper_limit < lower_limit:
    print("Please enter a valid upper and lower limit")
    quit()

random_number = random.randint(lower_limit, upper_limit)
print("The random number between {lower_limit} and {upper_limit} is: {random_number}")
print("All the Very Best! :)")
count=0
while True:
   userInput=int(input("Guess the number"))
   if userInput > random_number:
    print("Oops! The number you typed is greater than the actual number. :(")
    count+=1
    continue
   elif userInput < random_number:
    print("Oops! The number you typed is less than the actual number. Correct it. :(")
    count+=1
    continue
   else:
    print("Congratulations! You guessed the correct number. :)")
    break
print("you got in ", count, "guesses")