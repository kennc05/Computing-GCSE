GBPdict={'USD':1.66,'Euro':1.68,'Yen':172.83}
USDdict={'GBP':0.59,'GBP':0.60,'Yen':102.28}
Eurodict={'GBP':0.82,'USD':1.38,'Yen':141.91}
Yen={'GBP':0.0058,'USD':0.0098,'Euro':0.007}

currencyfrom=input('What would you like to convert from: ')

    
   
currencyto=input('What would you like to convert to: ')

amount=int(input('How much would you like to convert??: '))

if currencyfrom=='USD' and currencyto=='GBP':
        convertedamount=(amount*USDdict['GBP'])
        print('Thank you correct input, now converting')
        print('Your amount from $',amount,'to GBP is £',convertedamount)
        
