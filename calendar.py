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
elif

#Print and Format results
