import random 
def paper():
    l=["stone","paper","scissor"]
    computer=random.choice(l)
    print("You choosed 'Paper' and now computer chance")
    print("computer choice:",computer)
    
    if "stone" == computer:
        print("You won the game")
        
    elif "paper"== computer:
        print("Match drawn!!  Retry")
        
    else:
        print("You loose the game")