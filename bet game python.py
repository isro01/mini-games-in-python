import time
from random import randint
print "Welcome to the betting game"
print """
Instructions:
1. The computer will choose a number between 1 and 14
2. You choose a sign :>,<,or = 7. > represents a number >7 and so on.
3. If you choose > or < correctly you get twice the amount back.
4. If you choose = correctly, you get thrice the money back but if you loose,
   twice money gets taken away.
5. Play till you have $0. If you want to leave type "l" in after choose sign and any bet amount.
"""
money=100
while money>0:
    num=randint(0,14)
    print "Choose sign"
    ans=raw_input("")
    print "Enter bet amount"
    bet=int(raw_input(""))
    if ans=="l":
        print "ou have left with:$",money
        break
    elif ans==">" and num>7:
        money+=bet
        print "Money left:",money
        print "The number was",num
    elif ans=="<" and num<7:
        money+=bet
        print "Money left:",money
        print "The number was",num
    elif ans==">" and num<7:
        money-=(bet*2)
        print "Money left:",money
        print "The number was",num
    elif ans=="<" and num>7:
        money-=(bet*2)
        print "Money left:",money
        print "The number was",num
    elif ans=="=" and num==7:
        money=money+(bet*2)
        print "Money left:",money
        print "The number was",num
    elif ans=="=" and num!=7:
        money-=(bet*2)
        print "Money left:",money
        print "The number was",num
    else:
        print "Please read the instructions again and type correctly"
        
    
