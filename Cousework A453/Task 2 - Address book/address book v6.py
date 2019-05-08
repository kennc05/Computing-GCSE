#Version 6 of the code - changed whole code for efficiency
#Biggest change in history of coding omg
#Everythin works boyy its flawless
from csv import reader

file= reader(open('address.csv'))

rowselectresult=''

results=[]


def addressbook1(surname):
        print('looking for people with surname '+search)
        for row in file:
                surname=row[0]
                if surname==search:
                        results.append(row)
def addressbook2(date):
        print('looking for people with month of birth '+search)
        for row in file:
                date=row[6]
                dateseperate=date.split('/')
                month=dateseperate[1]
                if month==search:
                        results.append(row)
                        

rowselectresult=''
while True:
        try:
                rowselect = int(input('Please select what row you want to search 1)Surname 2)Month Of birth: '))

        except ValueError:
                print('No letters mate')
                continue
        if rowselect>0 and rowselect>2:
                print('Thats not really an option')
                continue
        else:
                break

search=input('Please enter what you are searching for ').title()
print('So you are looking for '+search)

if rowselect==1:
        rowselectresult='surname'
        addressbook1(rowselectresult)

if rowselect==2:
        rowselectresult='date'
        addressbook2(rowselectresult)


if len(results)==0:
    print('Unfortunately we found none :(')
    print(results)
    
else:
        print('Lucky you! We found stuff...') 
        print('Number of records= '+str(len(results)))
        count=0
        for i in results:
                count=count+1
                print('\nResult '+str(count)+' for search '+rowselectresult+' of '+search)
                print('Last Name: '+i[0]+'\n''First Name: '+i[1]+'\n''Address: '+i[2]+'\n''County: '+i[3]+'\n''Postcode: '+i[4]+'\n''Phone Number: '+i[5]+'\n''DoB: '+i[6]+'\n''Email: '+i[7])

