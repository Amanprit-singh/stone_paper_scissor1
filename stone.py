import random
def stone():
    l=["stone","paper","scissor"]
    computer=random.choice(l)
    print("You choosed 'Stone' and now computer chance")
    print("computer choice:",computer)
    
    if "stone" == computer:
        print("Match drawn!!  Retry")
    elif "paper"== computer:
        print("You loose the game")
        
    else:
        
        print("You won the game")