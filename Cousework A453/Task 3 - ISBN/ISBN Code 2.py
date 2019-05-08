#ISBN Attempt 4 + Improval and Simplified version
ISBN=input('Enter the 10 digit ISBN code, no characters!: ')

while len(ISBN)!= 10  or str.isalpha(ISBN)==True or str.isdigit(ISBN)==False:
                print('You have entered more / less than 10 digits or have entered characters')
                ISBN=[input('Please  enter a 10 digit ISBN code: ')]
else:
#Using the list function puts the inputted numbers into a list
                number1=int(ISBN[0])*11
                number2=int(ISBN[1])*10
                number3=int(ISBN[2])*9
                number4=int(ISBN[3])*8
                number5=int(ISBN[4])*7
                number6=int(ISBN[5])*6
                number7=int(ISBN[6])*5
                number8=int(ISBN[7])*4
                number9=int(ISBN[8])*3
                number10=int(ISBN[9])*2


#Range of the list starts from 0 - 9
total=number1+number2+number3+number4+number5+number6+number7+number8+number9+number10

print('Now calculating the ISBN')

divide=total%11

print('Divide '+str(total)+' with 11 gives 11 remainder '+str(divide))
print('Subtacting 11 from '+str(divide))
subtract=11-divide

ISBN.append(ISBN + subtract)
print (ISBN)

