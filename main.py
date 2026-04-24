# import random
# def stone():
#     l=["stone","paper","scissor"]
#     computer=random.choice(l)
#     print("You choosed 'Stone' and now computer chance")
#     print("computer choice:",computer)
    
#     if "stone" == computer:
#         print("Match drawn!!  Retry")
#     elif "paper"== computer:
#         print("You loose the game")
        
#     else:
        
#         print("You won the game")
     

# def paper():
#     l=["stone","paper","scissor"]
#     computer=random.choice(l)
#     print("You choosed 'Paper' and now computer chance")
#     print("computer choice:",computer)
    
#     if "stone" == computer:
#         print("You won the game")
        
#     elif "paper"== computer:
#         print("Match drawn!!  Retry")
        
#     else:
#         print("You loose the game")

# def scissor():
#     l=["stone","paper","scissor"]
#     computer=random.choice(l)
#     print("You choosed 'Scissor' and now computer chance")
#     print("computer choice:",computer)
    
#     if "stone" == computer:
#         print("You loose the match")
        
        
#     elif "paper"== computer:
#         print("You won the game")
        
        
#     else:
#         print("Match drawn!!  Retry")
    
from stone import stone
from paper import paper
from scissor import scissor

def main():
    while True:
        print("**************************")
        print("Stone Paper Scissor")
        print("**************************")
        print("\n1.Stone")
        print("\n2.Paper")
        print("\n3.Scissor")
        print("\n4.Exit")
        
        
        choice=int(input("Enter your choice:")) 
        
        
             
        if choice == 1:
            stone()
            
        elif choice == 2:
            paper()
            
        elif choice == 3:
            scissor()
            
        elif choice ==4:
            print("Thank you!! Have a nice day")
            return False
        else:
            print("Invalid choice")
            
main()