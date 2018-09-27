#Calender program
#9-26-2018

#Greeting
print("Welcome to the Calendar program.")

#User Input


#Determine Days (week and month)
century_digits = format(year/100, '.0f')
year_digits = year%100
value = year_digits+floor(year_digits/4)

if century_digits = 18:
  value = value + 2
elif century_digits = 20:
  value = value + 6
if month = 'January' and not (year%4==0):
  value = value + 1
elif month = 'February' and (year%4==0):
  value = value + 3
  if month = 'February' and not (year%4==0):
    value = value + 4
elif month = 'March' or month = 'November':
  value = value + 4
elif month = 'April' or month = 'July':
  value = value + 0
elif month = 'May':
  value = value + 2
elif month = 'June':
  value = value + 5
elif month = 'August':
  value = value + 3
elif month = 'October':
  value = value + 1
elif month = 'September' or month = 'December':
  value = value + 6
  
value = (value + day)mod 7

if value == 1:
  weekday = Sunday
if value == 2:
  weekday = Monday
if value == 3:
  weekday = Tuesday
if value == 4:
  weekday = Wednesday
if value == 5:
  weekday = Thursday
if value == 6:
  weekday = Friday
if value == 0:
  weekday = Saturday


#Print and Format results
