file = open ('currency.txt', 'rt')

lines = file.readlines()

num=0

for line in lines:
    splitline=line.split(' ')
    num+=1
    print('Option '+str(num)+': '+splitline[0])

option= int(input('What option would you like to choose: '))
amount= input('Enter the amount you want: ')

chosenline = lines[option]

currencies = chosenline.split(' ')

if option==1:
    exchange1=float(amount)*float(currencies[1].strip())
    print('$',exchange1)

if option==2:
    exchange2=amount*float(currencies[1].strip())
    print('€',exchange2)

if option==3:
    exchange3=amount*float(currencies[1].strip())
    print('¥',exchange3)

if option==4:
    exchange4=amount*float(currencies[1].strip())
    print('$',exchange4)

if option==5:
    exchange5=amount*float(currencies[1].strip())
    print('€',exchange5)

if option==6:
    exchange6==amount*float(currencies[1].strip())
    print('¥',exchange6)

if option==7:
    exchange7=amount*float(currencies[1].strip())
    print('£',exchange7)

if option==8:
    exchange8=amount*float(currencies[1].strip())
    print('$',exchange8)

if option==9:
    exchange9=amount*float(currencies[1].strip())
    print('¥',exchange9)

if option==10:
    exchange10=amount*float(currencies[1].strip())
    print('£',exchange10)

if option==11:
    exchange11=amount*float(currencies[1].strip())
    print('$',exchange11)

if option==12:
    exchange12=amount*float(currencies[1].strip())
    print('€',exchange12)
    
    
