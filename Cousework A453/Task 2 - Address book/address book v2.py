#Version 2 of the code - Basics with no added features
#Date works, but only when entered fully
from csv import reader

file= reader(open('address.csv'))

results=[]


rowselect = int(input('Please select what row you want to search \n0)Last name \n1)First Name \n2)Address \n3)Area \n4)Postcode \n5)Phone Number \n6)Date of Birth \n7)Email \nPlease only enter numbers!:'))


search = input('Please enter what you are searching for ')


if rowselect=='6':
    for row in file:
        date=row[6]
        if date==search:
            results.append(row)

else:            
    for row in file:
        if row[rowselect]==search:
            results.append(row)

if len(results)==0:
    print('We found none :(')
    
else:
    for i in results:
        print('Lucky you! We found stuff...')
        print('Results = '+str(len(results)))
        print('First Name: '+i[0]+'\n''Second Name: '+i[1]+'\n''Address: '+i[2]+'\n''Area: '+i[3]+'\n''Postcode: '+i[4]+'\n''Date of brith: '+i[5]+'\n''Email '+i[6])
