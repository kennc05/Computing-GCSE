#Version 1 of the code - Basics with no added features
from csv import reader

file= reader(open('address.csv'))

results=[]


rowselect = input('Please select what row you want to search \n0)Surname 6)Date \nPlease only enter numbers!:')


search = input('Please enter what you are searching for ')


if rowselect=='0':
    for row in file:
        surname=row[0]
        if search==surname:
            results.append(row)

if rowselect=='6':            
    for row in file:
        date=row[6]
        datesplit=date.split('/')
        month=datesplit[1]
        if month==search:
            results.append(row)

if len(results)==0:
    print('We found none :(')
    
else:
    for i in results:
        print('Lucky you! We found stuff...')
        print('Results = '+str(len(results)))
        print('First Name: '+i[0]+'\n''Second Name: '+i[1]+'\n''Address: '+i[2]+'\n''Area: '+i[3]+'\n''Postcode: '+i[4]+'\n''Date of brith: '+i[5]+'\n''Email '+i[6])
