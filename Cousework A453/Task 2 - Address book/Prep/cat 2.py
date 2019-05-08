from csv import reader

file= reader(open('bigcats.csv'))

results=[]


rowselect = int(input('Please select what row you want to search \n0)Animal name \n1)Area \n2)Name \n3)Habitat \n4)Continent \n5)Length \n6)Date \nPlease only enter numbers!:'))

search = input('what are you looking for?: ')




if rowselect=='6':
    for row in file:
        date=row[6]
        if date[6:10]==search:
            results.append(row)

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
        print('Animal: '+i[0]+'\n''Breed: '+i[1]+'\n''Name: '+i[2]+'\n''Habitat: '+i[3]+'\n''Country: '+i[4]+'\n''Size: '+i[5]+'\n''DOB: '+i[6])
