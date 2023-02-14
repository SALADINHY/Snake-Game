from random import randint
print("I'm thinking of a number between 1 and 100")
def level_check():
    level= input("Do you want play easy or hard: ").lower()
    if level =="easy":
        return 10
    elif level =="hard":
        return 5
    else:
        print("chose again you write wrong contruction")
        print("--------------")
        level_check()
turn=level_check()
answer = randint(1,100)
guess=0
print(f"you have {turn} turn to play")
while guess != answer:
    guess=int(input("Guess number: "))
    if guess > answer:
       print("To high")
       turn-=1
       print(f"you have {turn} attempts")
       print("--------------")
    elif guess < answer:
       print("To low")
       turn-=1
       print(f"you have {turn} attempts")
       print("--------------")
    elif guess == answer:
       print(f"Correct answer is {answer}")
    if turn == 0 :
        print("You lose this game")
        print(f"Correct is {answer}")
        exit()