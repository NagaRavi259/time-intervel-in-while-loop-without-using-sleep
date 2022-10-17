from datetime import datetime , timedelta

lm=(datetime.now()+timedelta(minutes=0))""" change the 2 with how many minutes that you want or 
you can specify in (days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
this will add time intervel for next intervel of each loop"""
while True:
    ti=datetime.now() # this will check the time in each loop
    if lm<=ti: 
        ## add Code that you want to run with intervel of time 
        lm=(datetime.now()+timedelta(minutes=2)) #this will add time intervel for next intervel
        """this will check weather the time crosses the specified time then 
        it will go into the loop and execute the code that we want to execute 
        at the end of loo it will add few more minutes to the present time and wait for next intervel"""
