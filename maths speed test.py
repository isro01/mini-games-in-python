from timeit import default_timer
from random import randint
import time
print "lets test your math solving speed"
def start():
    time.sleep(1.5)
    print "ready...set...GO..."
    time.sleep(0.25)
    start=default_timer()
    a=randint(3,25)
    b=randint(3,12)
    c=randint(13,30)
    def q1():
        print "Question1:What's the square of",a
        ans=int(raw_input("Type your ans:"))
        if ans==a**2:
            print "Correct"
        else:
            print "Wrong"
            q1()
    q1()
    def q2():
        print "Question2:What's the cube of:",b
        ans=int(raw_input("Type your ans:"))
        if ans == b**3:
            print "Correct"
        else:
            print "Wrong"
            q2()
    q2()

    def q3():
        print "Question3:Multiply the number by 7",c
        ans=int(raw_input("Type your ans:"))
        if ans == c*7:
            print "Correct"
        else:
            print "Wrong"
            q3()
    q3()
    duration = default_timer() - start
    print duration
    if duration<=10:
        print "\t You're quite fast"
    elif duration<=20:
        print "\t fast but not fast enough"
    elif duration<=30:
        print "\t You need to revise your tables"

    print "Thanks for playing"
start()      
