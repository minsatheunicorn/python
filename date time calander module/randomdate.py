import random
import time
def getrandomdate(startdate,enddate):
    print("printing random date between ", startdate,"and ", enddate )
    x=random.random()
    dateformat="%m/%d/%Y"
    starttime=time.mktime(time.strptime(startdate,dateformat))
    endtime=time.mktime(time.strptime(enddate,dateformat))
    randomtime=starttime+x*(endtime-starttime)
    randomdate=time.strftime(dateformat,time.localtime(randomtime))
    return randomdate
print("randomdate=",getrandomdate("1/1/2026","1/20/2026"))