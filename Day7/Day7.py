import random
List_Word=["condao","caychoi","concho","maytinh","tivi"]
random_word=random.choice(List_Word)
display=[]
check_end = False
lives=3
word_length=len(random_word)
for i in range(word_length):
    display+="_"
print(display)
while not check_end:
    guess = input("Guess the letter: ").lower()
    for position in range(word_length) :
        i=random_word[position]
        if i==guess:
           display[position]=i
    print(display)
    if guess not in random_word:
       lives-=1
       print(f"you have {lives} to guess")
       if lives==0:
           print("you're loser")
           exit()
    if "_" not in display:
            check_end=True
            print("You're winner")