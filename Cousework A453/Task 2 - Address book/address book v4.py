#Version 5 of the code - Goes with task requirements with only search for Surname + Month of date
# Works, however no validation
from csv import reader

file= reader(open('address.csv'))


results=[]


rowselect = input('Please select what row you want to search 1)Surname 2)Month Of birth: ')

            
search =input('Please enter what you are searching for ').title()

rowselectsurname=0
rowselectdob=6

if rowselect=='1':
    rowselect=rowselectsurname
    for row in file:
        if row[rowselectsurname]==search:
            results.append(row)

if rowselect=='2':
    rowselect=rowselectdob
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
        print('Results for '+str(len(results)))
        print('Last Name: '+i[0]+'\n''First Name: '+i[1]+'\n''Address: '+i[2]+'\n''County: '+i[3]+'\n''Postcode: '+i[4]+'\n''Phone Number: '+i[5]+'\n''DoB: '+i[6]+'\n''Email: '+i[7])

