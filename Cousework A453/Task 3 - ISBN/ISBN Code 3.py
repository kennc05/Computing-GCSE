ISBN=input('Please enter the 10 digit ISBN number: ')
ISBNLength=10 #Sets the value for the length
#The different conditions
while len(ISBN)>ISBNLength and ISBN.isdigit()==True:
        print('You entered more than 10 digits')
        ISBN=input('Try again, entering no more than 10 digits only. From 0-9: ')
        
while len(ISBN)<ISBNLength and ISBN.isdigit()==True:
        print('You entered less than 10 digits')
        ISBN=input('Try again, entering no more than 10 digits only. From 0-9: ')

while len(ISBN)>ISBNLength and ISBN.isalpha()==True:
        print('You entered more than 10 letters, that is invalid')
        ISBN=input('Try again, entering no characters and only digits from 0-9: ')

while len(ISBN)<ISBNLength and ISBN.isalpha()==True:
        print('You entered less than 10 letters, that is invalid')
        ISBN=input('Try again, entering no characters and only digits from 0-9: ')

while len(ISBN)==ISBNLength and ISBN.isalpha()==True:
        print('You entered 10 letters, that is invalid')
        ISBN=input('Try again, entering no characters and only digits from 0-9: ')
        
while ISBN.isdigit()==False:
        print('Numbers and letters have been entered')
        ISBN=input('Try again, entering no characters and only digits from 0-9: ')
else:
        print('Thank you, you entered valid data, now calculating')
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
#Addition adds all the numbers multiplied together    
        addition=number1+number2+number3+number4+number5+number6+number7+number8+number9+number10

        divide=addition%11 #Finds the remainder of the sums divided by 11

        checkdigit=11-divide #Finds the check digit by doing the 11 - the answer to 'divide'
        if checkdigit==10: #Using the if function, if the sum equals 11, then make it 'X'
            checkdigit='X' #Replaces the checkdigit into an 'X'
            print('The check digit result equaled 10 so it will be put in as X')
        ISBNnumber=str(ISBN)+str(checkdigit) #Puts the two variables together in one line
        print('Your ISBN number is: ' + ISBNnumber) #Prints the message and the ISBN
