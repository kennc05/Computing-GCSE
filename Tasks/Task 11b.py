import random
#Import a random number for selecting a name

names=[] #LIst of names...

for i in range(0,5):
    names.append(input("Please enter a name: "))#Add entries (names) to the list

x=random.randint(0,4) #Get the random number between 0 and 4

print(names[x]+" is the winner!") #Output the winner!
