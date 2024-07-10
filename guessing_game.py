import random as rand

count = 0
Max_number = input("Input the maximum number for this game: ")

if Max_number.isdigit():
    Max_number = int(Max_number)
    if int(Max_number) <= 0:
        print("Please input a positive number")

    else: 
        random_number = rand.randint(0, Max_number)   

        while True:
            count += 1

            guess = input("Input your guess: ")

            if guess.isdigit() == True:
                guess = int(guess)

            else:   
                print("Please input a number: ")
                continue
           
            if guess == random_number:
                print("You got it right,You have tried", count ,"times")
                break

            elif guess > random_number:
                print("You guessed too high, you have guessed", count, "times")
                print(random_number)
                continue
            
            else :
                print("You guessed too low, you have guessed", count, "times" )
                continue
        
            
        
else:
    print("Please input a number")

print(random_number)