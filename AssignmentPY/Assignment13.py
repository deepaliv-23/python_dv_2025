# Secret number
secret_number = 7

# Loop to keep asking until guessed correctly
while True:
    guess = int(input("Guess the secret number: "))
    if guess == secret_number:
        print("Congratulations! You guessed it right.")
        break
    else:
        print("Try again!")
