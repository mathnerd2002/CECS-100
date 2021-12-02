now  = 2021
inp = input(‘Enter age of applicant:’)
age = int(inp)
if age < 16:
	print(‘cannot qualify for a license’)
elif age >= 16 and age < 18:
	print(‘qualifies for a provisional license’)
elif age >= 18 	and age <= 70:
	print(‘qualifies for a license’)
	print(‘must renew license 4 years from now in the year’)
	renewdate = now + 4
	print(renewdate)
else:
	age >= 70:
		print(‘must renew license next year in the year’)
		renewdate = now + 1
		print(renewdate)
