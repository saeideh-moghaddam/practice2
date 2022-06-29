import math

number = int (input(" Please type the number : "))

list=[]


for i in range (number) :
       if i==0 or i == 1 :
               list.append(1)
       else :
               fibo = list[i - 1] + list[i - 2]
               list.append(fibo)       
print(list) 