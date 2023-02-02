import time
import winsound
import os
 
h=1000000
while True :
    frequency = 2500  
    duration = 1000     
    e = input('press ENTER')
    for i in range(15):
        print (i,"\n")
        winsound.Beep(frequency, duration)
        os.system('cls' if os.name=='nt' else 'clear')
        
        #time.sleep(1.0)
    frequency = 2000  
    duration = 1250 
    winsound.Beep(frequency, duration)
    print("Started")
    if(e=='r'):
        h=1000000
    t1 = time.time()
    print()
    print()
    e = input('press ENTER for end')
    if(e=='r'):
        h=1000000
    t2 = time.time()
    print()
    print('Stopped')
    print()
    if(h>t2-t1):
        h=t2-t1
    print('Solve Time: ',t2-t1)
    print('Minimum Time:',h)
    time.sleep(2.0)
    os.system('cls' if os.name=='nt' else 'clear')




