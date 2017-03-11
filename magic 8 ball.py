from random import randint
print "Welcome to Python Magic 8 ball"
print "/t Ask a question"
def start():
    question=raw_input("Type:")
    num=randint(0,8)
    if question=="":
        print "Please type a question"
    elif num==1:
        print "I think yes"
    elif num==2:
        print "The answer is a little hazy...Ask again"
    elif num==3:
        print "Oh yes definitely"
    elif num==4:
        print "OH oh, I see trouble"
    elif num==5:
        print "The spirits are busy right now...Go away"
    elif num==6:
        print "Nope...Not even in your wildest dreams..."
    elif num==7:
        print "I say go for it"
    elif num==8:
        print "HMMMM I sense dark magic.Tread carefully"
    print "Thanks for playing.."
    q=raw_input("want to ask another question...Y or N :")
    if q=="Y":
        start()
    else:
        print "I was busy anyway..."
start()
