#Version 1 of the code - basics can search
from csv import reader

file= reader(open('address.csv'))

results=[]



rowselect = input('Please select what row you want to search \n0)Last Name \n1)First Name \n2)Address \n3)Area \n4)PostCode \n5)Number \n6)Date of birth \n7)Email \nPlease only enter numbers!:')

search = input('what are you looking for?: ')

    
print('So you chose '+search+'!')

for row in file:

    if row[int(rowselect)]==search:
        results.append(row)

if len(results)==0:
    print('We found nothing :( Try again!')

else:
    for i in results:
        print(i)
