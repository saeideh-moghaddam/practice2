import random

dice = random.randint(1,6)

print("dice :" , dice)

if dice == 6 :
    dice = random.randint(1,6)
    print (" you have a prize")

    print("dice :" , dice)

else:
    print ("end the app!")