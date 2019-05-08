file = open ('currencies v2.txt', 'rt')

lines = file.readlines()

numbercount=0

for line in lines:
    splitline=line.split('-')
    print('Option '+str(numbercount)+': '+splitline[0])
    numbercount+=1


while True:
    try:
        option= int(input('What option would you like to choose: '))

    except ValueError:
        print('You did not enter an interger! Try again')
        continue
    if option>0 and option>11:
        print('Sorry thats not part of the options. Please enter an option between 1-11')
        continue
    else:
        break
    
while True:
    try:
        amount= float(input('Enter the amount you want: '))
    
    except ValueError:
        print('You did not enter an interger! Try again')
        continue
    else:
        break


chosenline = lines[option]
currency_addons= chosenline.split(' ')
exchangedrate=amount*float(currency_addons[4])
roundedrate=str(round(exchangedrate,2))

print('You chose to convert '+str(currency_addons[5].strip())+''+str(amount)+' '+str(currency_addons[1])+' '+str(currency_addons[2]))

convertedamount=str(currency_addons[6].strip()) + str(roundedrate)

print('This came out as '+convertedamount)

