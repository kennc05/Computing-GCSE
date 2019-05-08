#Version 4 of the code - Goes with task requirements with only search for Surname + Date

# This code works when searching for surname but not year!!!

from csv import reader

file= reader(open('address.csv'))


results=[]


rowselect = input('Please select what row you want to search 1)Surname 2)Date Of birth')
search =input('Please enter what you are searching for ')

rowselectsurname=0
rowselectdob=6

if rowselect=='1':
    rowselect=rowselectsurname

if rowselect=='2':
    rowselect=rowselectdob

else:
           
    for row in file:
        date=row[6]
        if row[rowselect]==search:
            results.append(row)


if len(results)==0:
    print('We found none :(')
    
else:
    for i in results:
        print('Lucky you! We found stuff...')
        print('Results = '+str(len(results)))
        print('Last Name: '+i[0]+'\n''First Name: '+i[1]+'\n''Address: '+i[2]+'\n''Area: '+i[3]+'\n''Postcode: '+i[4]+'\n''Date of brith: '+i[5]+'\n''Email '+i[6])

