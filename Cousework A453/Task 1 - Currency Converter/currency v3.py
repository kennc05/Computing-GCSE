file = open ('currencies v2.txt', 'rt')

lines = file.readlines()

numbercount=0

for line in lines:
    splitline=line.split('-')
    print('Option '+str(numbercount)+': '+splitline[0])
    numbercount+=1

option= int(input('What option would you like to choose: '))
amount= int(input('Enter the amount you want to convert: '))

chosenline = lines[option]


currencynames= chosenline.split(' ')


exchangedrate=amount*float(currencynames[4])
print('You chose to convert '+currencynames[1]+' to '+currencynames[2])
convertedamount=str(currencynames[6].strip()) + str(exchangedrate)

print('This came out as '+convertedamount)
