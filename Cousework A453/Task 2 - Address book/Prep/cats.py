from csv import reader

file=reader(open('bigcats.csv'))

results=[]



rowselect = int(input('Please select what row you want to search \n0)Animal name \n1)Area \n2)Name \n3)Habitat \n4)Continent \n5)Length \n6)Date \nPlease only enter numbers!:'))

search = input('what are you looking for?: ')

if rowselect=='6':
    month = search.split('/')

else:
    
    print('So you chose'+search+'!')

    for row in file:
        if row[rowselect]==search:
            results.append(row)

    if len(results)==0:
        print('We found nothing :( Try again!')

    else:
        for i in results:
            print(i)
