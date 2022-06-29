import math

student = int(input("please type the number of class student : "))

list=[]


for i in range (student): 
  lessons= float(input("please type the students grades scores : "))
  list.append(lessons )
  


b = sum(list)

average = b / student

print (average)

maximum=max (list)
print ( " max class scores :", maximum)

minimum=min (list) 
print("min class scores :", minimum )