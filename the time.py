import math
import time
hour = int (input(" Please type the hour :"))
minute = int (input(" Please type the minute :"))
second = int (input( "Please type the second :"))

while  hour > 12 or minute > 59 or second > 59 :
        print ("no more than 12 hour or no more than 59 minute or no more than 59 second , please try again")
        hour = int (input(" enter a oclock :"))
        minute = int (input(" enter a minute :"))
        second = int (input( "enter a second :"))
    

print (hour ," :" ,minute , " :" , second , )
c = hour * 3600
m= minute * 60
s= c + m + second 

print (s)