from random import randint

print "\t \t WELCOME!!! to Guess the Number game"
print "\t High means your guess is higher than the answer"
print "\t Low means your guess is lower than the answer"
print "The number has been chosen by the Computer and it is between 0 and 10"
def start():
    num_generated = randint(0,11)
    for turn in range(3):
        print "Turn",turn+1
        ans=int(raw_input("Guess the number:"))

        if turn+1==3:
            print "GAME OVER"
            print "The correct ans is",num_generated
        elif ans == num_generated:
            print "Congratulations, you won the GAME!!!"
            break
        elif ans>num_generated:
            print "High"
        elif ans<num_generated:
            print"Low"

    print "Want to play again..Y or N"
    ans1=raw_input("")
    if ans1=="Y":
        start()
    elif ans1=="N":
        print "OKAY SEE YOU LATER!!!"
    else:
        print "Please answer in Y or N only"
start()


    
    
    
    
