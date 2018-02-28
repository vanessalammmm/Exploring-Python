# Practising regex w a format checker for personal particulars

import re

print('First, please input your name:')
my_name=str(input())

print('Thank you. Now please input your local contact number')
string=str(input('+65'))

phone=re.compile('(9|8|6)\d{7}')
validnumber=phone.match(string)

while validnumber == None:
	print('Invalid number! Please input again')
	string=str(input())
	validnumber=phone.match(string)

if validnumber != None:
	print('Your number: ' + validnumber.group()+' has been recorded. Next, please type your IC number:')


my_ic=str(input())

validic=re.compile('(s)\d{7}([a-z])',re.I)
validic=validic.match(my_ic)

while validic==None:
	print('Invalid IC number! Please input again')
	my_ic=str(input())
	validic=re.match('(s|S)\d{7}([a-zA-Z])',my_ic)

if validic !=None:
	print('Your ic number: '+validic.group()+' has been recorded. Next, please type your email address: ')


my_email=str(input())
validemail=re.match('([a-zA-Z0-9._])+@([a-zA-Z])+\.([a-zA-Z]){2,4}', my_email)

while validemail==None:
	print('Invalid email! Please input again:')
	my_email=str(input())
	validemail=re.match('([a-zA-Z0-9._])+@([a-zA-Z])+\.([a-zA-Z]){2,4}', my_email)

if validemail!=None:
	print ('Thank you. Your email: '+validemail.group()+' has been recorded.')

print('\nPlease check that all particulars are correct:\n'
	+'\nName: '.ljust(20)+my_name.rjust(22)
	+'\nContact Number: '.ljust(20)+validnumber.group().rjust(22)
	+'\nIC number: '.ljust(20)+validic.group().rjust(22)
	+'\nEmail address: '.ljust(20)+validemail.group().rjust(22))
