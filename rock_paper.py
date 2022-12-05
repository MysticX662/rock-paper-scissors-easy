import random
choices=["rock","paper","scissors"]
user_points=0
npc_points=0
rounds=int(input("how many points is needed to win?:"))
while True:
    npc_action=random.choice(choices)
    user_action = input("rock paper or scissors?:")
    print(f"\nYou chose {user_action}, computer chose {npc_action}.\n")
    if user_action==npc_action:
        print("tie, no points")
    
        print("you have", user_points, "points")

        print("computer has", npc_points, "points")
        print("____________________________________________________________________________")
        if user_points==rounds:
            print("____________________________________________________________________________")
            print("user won the game!")
            print("____________________________________________________________________________")
        elif npc_points==rounds:
            print("____________________________________________________________________________")
            print("computer won the game!")
            print("____________________________________________________________________________")
    elif user_action=="rock" and npc_action=="paper":
        print("computer wins!")
        npc_points=npc_points+1
        print("you have", user_points, "points")

        print("computer has", npc_points, "points")
        print("____________________________________________________________________________")
        if user_points==rounds:
            print("____________________________________________________________________________")
            print("user won the game!")
            print("____________________________________________________________________________")
        elif npc_points==rounds:
            print("____________________________________________________________________________")
            print("computer won the game!")
            print("____________________________________________________________________________")
    elif user_action=="rock" and npc_action=="scissors":
        print("user wins!")
        user_points=user_points+1
        print("you have", user_points, "points")

        print("computer has", npc_points, "points")
        print("____________________________________________________________________________")
        if user_points==rounds:
            print("____________________________________________________________________________")
            print("user won the game!")
            print("____________________________________________________________________________")
        elif npc_points==rounds:
            print("____________________________________________________________________________")
            print("computer won the game!")
            print("____________________________________________________________________________")
    elif user_action=="paper" and npc_action=="scissors":
        print("computer wins!")
        npc_points=npc_points+1
        print("you have", user_points, "points")

        print("computer has", npc_points, "points")
        print("____________________________________________________________________________")
        if user_points==rounds:
            print("____________________________________________________________________________")
            print("user won the game!")
            print("____________________________________________________________________________")
        elif npc_points==rounds:
            print("____________________________________________________________________________")
            print("computer won the game!")
            print("____________________________________________________________________________")
    elif user_action=="paper" and npc_action=="rock":
        print("user wins!")
        user_points=user_points+1
        print("you have", user_points, "points")

        print("computer has", npc_points, "points")
        print("____________________________________________________________________________")
        if user_points==rounds:
            print("____________________________________________________________________________")
            print("user won the game!")
            print("____________________________________________________________________________")
        elif npc_points==rounds:
            print("____________________________________________________________________________")
            print("computer won the game!")
            print("____________________________________________________________________________")
    elif user_action=="scissors" and npc_action=="paper":
        print("user wins!")
        user_points=user_points+1
        print("you have", user_points, "points")

        print("computer has", npc_points, "points")
        print("____________________________________________________________________________")
        if user_points==rounds:
            print("____________________________________________________________________________")
            print("user won the game!")
            print("____________________________________________________________________________")
        elif npc_points==rounds:
            print("____________________________________________________________________________")
            print("computer won the game!")
            print("____________________________________________________________________________")
    elif user_action=="scissors" and npc_action=="rock":
        print("computer wins!")
        npc_points=npc_points+1
        print("you have", user_points, "points")

        print("computer has", npc_points, "points")
        print("____________________________________________________________________________")
        if user_points==rounds:
            print("____________________________________________________________________________")
            print("user won the game!")
            print("____________________________________________________________________________")
        elif npc_points==rounds:
            print("____________________________________________________________________________")
            print("computer won the game!")
            print("____________________________________________________________________________")
    elif user_action=="stop":
        exit()
    else:
        print("please only use \"rock\" \"paper\" or \"scissors\"")
        print("____________________________________________________________________________")
        if user_points==rounds:
            print("____________________________________________________________________________")
            print("user won the game!")
            print("____________________________________________________________________________")
        elif npc_points==rounds:
            print("____________________________________________________________________________")
            print("computer won the game!")
            print("____________________________________________________________________________")
