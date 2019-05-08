names=[]
entry=''
count=0 #Count starts from 0 until the first name is entered
while entry!='END':
    entry=input('Please enter a name: ')
    names.append(entry)
    count=count+1

count=count-1 #Get rid of END as it isn't a name
names.pop() #Gets rid of END from the list

print('You have entered '+str(count)+' names.')
print(names) #Prints the names in a list
