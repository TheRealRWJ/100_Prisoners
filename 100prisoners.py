# Setup:
# 100 prisoners numbered 1-100
# Slips with their numbers are randomly placed in 100 boxes in a room
# Each prisoner may enter the room one at the time and check 50 boxes
# The must leave the room exc actly as they found it and can't communicate with the others after
# If all prisoners find ther number during their turn in the room they will all be freed
# but if even 1 fails, they will all be executed

# Veritasium Video: https://www.youtube.com/watch?v=iSNsgj1OCLA



import random


debug = 0


def CheckTheBox(prisoner,tries,box,number):
    if (debug): print ( 'Prisoner',prisoner, tries,box,'->', number)
    if (prisoner == number): 
        print ("Prisoner", prisoner, "is very happy with try", tries)

def Average(lst):
    return sum(lst) / len(lst)

# Lets get som percentages

MaxRuns = 1000
AllLuckyPrisoners = []

for run in range(MaxRuns):
        
    # Setting up the room
    prisoners = range(1,101)
    numbers = []
    boxes = []
    LuckyPrisoners = 0

    for n in range(0,101):
        numbers.append(n)
        if (debug): print(numbers[n-1], end=" ")

    # Fill the boxes
    boxes = numbers[:]
    random.shuffle(boxes)
    if (debug):
        print ('\n')
        for c in range(0,101):
            print(boxes[c], end=" ")


    # Prisoner in the room
    LuckyPrisoners = []
    for p in prisoners:
        tries = 50
        nextbox = random.randrange(0,101)
    
        while tries > 0:
            tries-=1
            box = nextbox
            nextbox = boxes[nextbox]
            #CheckTheBox(p,tries,box,nextbox)
            if nextbox == p: 
                LuckyPrisoners.append(p)
                break
    AllLuckyPrisoners.append(len(LuckyPrisoners))
""" 
    print ("This prison had", len(LuckyPrisoners), "lucky prisoners")
    print ("The luckyprisoners are:")
    for p in range(len(LuckyPrisoners)):
        print(LuckyPrisoners[p], end = " ") 
"""
    
print ("Number of runs", MaxRuns)
print ("Average number of lucky prisoners", Average(AllLuckyPrisoners))
AllLuckyPrisoners.sort()
print ("Highest number of lucky prisoners",AllLuckyPrisoners[-1])

print ("\n")
