import random

user_wins = 0
pc_wins = 0
options=["rock", "paper", "scissor"]
while True:
    user_input = input("Type rock/paper/scissor or Q to quit:").lower()
    if user_input == "q":
        break
        
    if user_input not in options:
        continue
    
    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissor: 2
    pc_pick = options[random_number]
    print("computer picked", pc_pick + ".")
    #rock-----------------------------------------
    if user_input == "rock" and pc_pick =="scissor":
        print ("you won!")
        user_wins += 1
        continue
    if user_input == "rock" and pc_pick =="paper":
        print ("you lose!")
        pc_wins += 1
        continue
    if user_input == "rock" and pc_pick =="rock":
        print ("Its a tie!")
        continue
    #----------------------------------------------
    #paper-----------------------------------------
    if user_input == "paper" and pc_pick =="rock":
        print ("you won!")
        user_wins += 1
        continue
    if user_input == "paper" and pc_pick =="scissor":
        print ("you lose!")
        pc_wins += 1
        continue
    if user_input == "paper" and pc_pick =="paper":
        print ("Its a tie!")
        continue
    #-----------------------------------------------
    #scissor----------------------------------------
    if user_input == "scissor" and pc_pick =="paper":
        print ("you won!")
        user_wins += 1
        continue
    if user_input == "scissor" and pc_pick =="rock":
        print ("you lose!")
        pc_wins += 1
        continue
    if user_input == "scissor" and pc_pick =="scissor":
        print ("Its a tie!")
        continue
    
print("you won", user_wins, "times.")
print("pc won", pc_wins, "times.")
print("Bye")
