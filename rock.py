from random import randrange

player_1=(input("User 1 Please enter your name: ")) #takes player1 Name
player_2="Computer"
rock=0 
sessiors=1
paper=2
player_1_choice=(int(input("dear "+player_1+" Please choose your option: ")))
player_2_choice=randrange(rock,paper)
winner_1=0
winner_2=0

print(player_1,"Choice is ",player_1_choice)
print(player_2,"Choice is ",player_2_choice)

if player_1_choice==0 and player_2_choice==1 or player_1_choice==1 and player_2_choice==2:
    print("The winner is:",player_1)
    winner_1=winner_1+1
    print("Hey",player_1,"your score is: ",winner_1)
elif player_1_choice==2 and player_2_choice==0:
    print("The winner is:",player_1)
    winner_1=winner_1+1
    print("Hey",player_1,"your score is: ",winner_1)       
elif player_1_choice==1 and player_2_choice==0 or player_1_choice==1 and player_2_choice==1:
    print("The winner is:",player_2)
    winner_2=winner_2+1
    print("The",player_2,"your score is: ",winner_2)
elif player_1_choice==1 and player_2_choice==2:
    print("The",player_2,"your score is: ",winner_2)
    iwinner_2=winner_2+1
    print(winner_2)
else:
    print("Tie")






