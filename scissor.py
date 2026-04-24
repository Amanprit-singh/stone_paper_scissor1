import random 
def scissor():
    l=["stone","paper","scissor"]
    computer=random.choice(l)
    print("You choosed 'Scissor' and now computer chance")
    print("computer choice:",computer)
    
    if "stone" == computer:
        print("You loose the match")
        
        
    elif "paper"== computer:
        print("You won the game")
        
        
    else:
        print("Match drawn!!  Retry")