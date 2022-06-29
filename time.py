import math
import time

s = int(input("please type the second : "))


hour =  s // 3600
minute = s % 60
second =  minute - hour

print(hour ,":", minute, ":",second )