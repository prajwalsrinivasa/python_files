import time
import calendar

ticks =time.time()
print ("the no",ticks)
localtime=time.asctime(time.localtime(time.time()))
print (localtime)
exact=localtime.split(" ")
print(exact)
print(exact[3])
if exact[3] is '23:33:00':
    print ("tushar drink water")

    
cal =calendar.month(2012,12)
print (cal)
