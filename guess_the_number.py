import random

def guess_the_no():
    print("Welcome to 'GUESS THE NUMBER'")
    print("Guess a number between 1 and 100")
    secret_no = random.randint(1, 100)
    attempt = 0
    max_attempt = 3  
 
    while attempt < max_attempt:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Invalid number")
            continue

        attempt = attempt + 1

        if guess < secret_no:
            print("Too low")
        elif guess > secret_no:
            print("Too high")
        else:
            print(f"You guessed it correctly in {attempt} attempt(s)!")
            return
            
    print(f"Game over... the number was {secret_no}")

if __name__ == "__main__":
    guess_the_no()