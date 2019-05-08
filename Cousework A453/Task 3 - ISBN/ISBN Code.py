#ISBN Attempt 3.0
number1=int(input('Enter a number: '))
number2=int(input('Enter a number: '))
number3=int(input('Enter a number: '))
number4=int(input('Enter a number: '))
number5=int(input('Enter a number: '))
number6=int(input('Enter a number: '))
number7=int(input('Enter a number: '))
number8=int(input('Enter a number: '))
number9=int(input('Enter a number: '))
number10=int(input('Enter a number: '))

total=number1*11,number2*10,number3*9,number4*8,number5*7,number6*6,number7*5,number8*4,number9*3,number10*2
total2=number1*11+number2*10+number3*9+number4*8+number5*7+number6*6+number7*5+number8*4+number9*3+number10*2

print('Each of the numbers inputted gives: '+str(total))
print('Now calculating the ISBN')
divide=total2%11
print('Divide '+str(total2)+' with 11 gives 11 remainder '+str(divide))
isbnno=int(input('Enter the remainder of that number: '))
subtract=11-isbnno
print(number1,number2,number3,number4,number5,number6,number7,number8,number9,number10,subtract)

