import time
from timeit import default_timer
print "Let's play a typing speed game"
time.sleep(0.35)
print "Press enter 50 times and see your types per second result"
time.sleep(1.5)
print "ready...set...GO..."
score=0
count=50
start=default_timer()
while count>0:
    type=raw_input("")
    if type=="":
        score+=1
    count-=1
print "Over"
print"Calculating..."
time.sleep(1)

end=default_timer()-start
print end
calc=float(50)/end
print "Types per seconds:",calc


