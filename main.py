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
