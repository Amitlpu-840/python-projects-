import random

# user guessing program
print("here you'll have to guess the number")


def guess(x):
    random_number = random.randint(1, x)
    print(random_number)
    y = 0
    while y != random_number:
        y = int(input(f"guess the number between 1 to {x}: "))
        if y < random_number:
            print("oops! your guess is low.. guess again ")
        elif y > random_number:
            print("oops! your guess is high.. guess again ")
    print(f"nice! you guessed the right number which was {y}")


guess(10)


# computer guessing program

print("here I'll guess the number which you have assumed ")


def computer_guess(x):
    low = 1
    high = x
    temp = 0
    feedback = ""
    print(f"guessing the number between {low} and {high} ")
    while feedback != "y" and low != high:
        g = random.randint(low, high)
        feedback = input(
            f"is {g} a high guess or a low guess or a correct guess?(h/l/y)"
        )
        if feedback == "h":
            high = g - 1
        elif feedback == "l":
            low = g + 1
        temp += 1
    print(f"Nice! I have guessed you number in {temp} attempts ")


y = int(input(f"Your range is from 1 to which number ? "))
computer_guess(y)
