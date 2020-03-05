AI_NAME = 'jarvis'
username = 'joan'
trust_level = 0
age = None
gender = None
email=None

print( f'Hello, {username}, my name is {AI_NAME}' )

print('your level is:', trust_level)

print("I want to do some questions")

str_age = input('how old are you?:')
if( str_age != ''):
	trust_level = trust_level + 1
	age = int(str_age)

str_gender = input('What is your gender? (m or f):')
if( str_gender != ''):
	if str_gender == 'm':
		gender = 'Male'
		trust_level = trust_level + 1
	elif str_gender == 'f':
		gender = 'Female'
		trust_level = trust_level + 1
	else:
		print(f'({str_gender}) does not exist in my database ')

str_email = input('What is  your e-mail?:')
if str_email != '':
	trust_level = trust_level + 1
	email = str_email

print ('thank for beliver in me')
print('this is your finally level',trust_level)