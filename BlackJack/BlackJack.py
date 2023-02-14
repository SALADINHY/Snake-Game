
from distutils.command.check import check
import random
user_cards=[]
comp_cards=[]
check_nextgame=True
check_BJ=False
def winner(result_user,result_comp):
    if result_user > 21 and result_comp >21:
        print("Draw this game")
    elif result_user > 21 and result_comp <= 21:
        print("You are loser")
    elif result_user <= 21 and result_comp > 21:
        print("You are winner")
    elif result_user > result_comp:
        print("You are winner")
    elif result_user < result_comp:
        print("You are loser")
    else:
        print("Draw this game")
def Dealcard():
    cards = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
    card = random.choice(cards)
    return card
def calculator(player):
    result=0
    for i in player:
        if i == "J" or i =="Q" or i=="K":
            i=10;
            result+=i
        elif i == "A" and player.__len__()>2:
            i=1
            result+=i
        elif i == "A" and player.__len__()==2:
            i=11
            result+=i
        else: 
            result+=i
    return result
def Computer_card(result):
    while result < 17:
        new_cards=Dealcard()
        comp_cards.append(new_cards)
        if new_cards == "J" or new_cards =="Q" or new_cards=="K":
            new_cards=10;
            result+=new_cards
        elif new_cards == "A" and comp_cards.__len__()>2:
            new_cards=1
            result+=new_cards
        elif new_cards == "A" and comp_cards.__len__()==2:
            new_cards=11
            result+=new_cards
        else:
            result+=int(new_cards)
    return result
def BlackJack(player):
    result=0
    for i in player:
        if i == "A" and player.__len__()==2:
            i=11
            result+=i
        elif i == "J" or i =="Q" or i=="K" or i =="10":
            i=10;
            result+=i
    if result == 21:
        print(f"{player} have black jack!!")
        check_BJ=True
    else:
        check_BJ=False
    return check_BJ
while check_nextgame==True:
    for i in range(2):
        user_cards.append(Dealcard())
        comp_cards.append(Dealcard())
    print(f"your cards: {user_cards}")
    print(f"Computer cards: {comp_cards}")
    user_BJ=BlackJack(user_cards)
    comp_BJ=BlackJack(comp_cards)
    if user_BJ==True and comp_BJ==False:
        print("You are winner")
        exit()
    elif user_BJ==False and comp_BJ==True:
        print("You are loser")
        exit()
    elif user_BJ==True and comp_BJ==True:
        print("Draw this game")
    check_continue=True
    while check_continue:
        DealCheck=input("Do you want to deal next card (type 'y' to deal next card or type 'n' dont need it): ").lower()
        if DealCheck=="y":
            user_cards.append(Dealcard())
            print(f"your cards: {user_cards}")
        else:
            check_continue=False
            user_result=calculator(user_cards)
    comp_result=calculator(comp_cards)
    comp_new=Computer_card(comp_result)
    print(f"Computer cards: {comp_cards}")
    winner(user_result,comp_new)
    text_check=input("Type 'y' to continue play this game or tyoe 'n' to exit: ").lower()
    if text_check == "y":
        check_nextgame=True
        user_cards=[]
        comp_cards=[]
    else:
        check_nextgame=False
