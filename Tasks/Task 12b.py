sentence = 'The cat sat on the mat.' #Defines the sentence variable
count=0 #Set the count as 0
for letter in sentence:
    if letter=='a':
        count=count+1 #Adds 1 to the count when 'a' is found

print('There are '+str(count)+' of the letter \'a\'') #Print
