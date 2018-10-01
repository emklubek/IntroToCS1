#Calender program
#9-26-2018

#Greeting
print("Welcome to the Calendar program.")

#User Input
month = input("Please enter a month. (Format like January, February, March, etc.)")
year = float(input("Please enter a year between 1800 and 2099."))

#Determine Days in Month
if month in('January', 'March', 'May', 'July', 'August', 'October', 'December'):
    days = 31
elif month in('April', 'June', 'September', 'November'):
    days = 30
elif month == 'February':
    if year%4==0:
        days = 29
    else:
        days = 28
else:
    print("Error: The month you entered is not in correct format.")
    days = 0

#Determine Days of Week
century_digits = format(year/100, '.0f')
year_digits = year%100
value = year_digits+(year_digits//4)

if century_digits == 18:
  value = value + 2
elif century_digits == 20:
  value = value + 6
if month == 'January' and not (year%4==0):
  value = value + 1
elif month == 'February' and (year%4==0):
  value = value + 3
  if month == 'February' and not (year%4==0):
    value = value + 4
elif month == 'March' or month == 'November':
  value = value + 4
elif month == 'April' or month == 'July':
  value = value + 0
elif month == 'May':
  value = value + 2
elif month == 'June':
  value = value + 5
elif month == 'August':
  value = value + 3
elif month == 'October':
  value = value + 1
elif month == 'September' or month == 'December':
  value = value + 6
  
value = (value + day)%7

#Print and Format results
print((format(month, ' >50')), (format(year, ' <50')))
print("Sun \t Mon \t Tue \t Wed \t Thu \t Fri \t Sat")
counter = 1
if days = 31:
  if value == 1:
    while counter <= 31:
      if counter == 29:
        print(counter, "\t", counter+1, "\t", counter+2)
        counter = counter + 7
      else:
        print(counter, "\t", counter+1, "\t", counter+2, "\t", counter+3, "\t", counter+4, "\t", counter+5, "\t", counter+6)
        counter = counter + 7
  elif value == 2:
    print("\t", counter,"\t", counter+1, "\t", counter+2, "\t", counter+3, "\t", counter+4, "\t", counter+5)
    counter = counter + 6
    while counter <= 31:
      if counter == 28:
        print(counter, "\t", counter+1, "\t", counter+2, "\t", counter+3)
        counter = counter+7
      else:
        print(counter, "\t", counter+1, "\t", counter+2, "\t", counter+3, "\t", counter+4, "\t", counter+5, "\t", counter+6)
        counter = counter + 7
  elif value == 3:
    print("\t\t", counter, "\t", counter+1, "\t", counter+2, "\t", counter+3, "\t", counter+4)
    counter = counter +5
    while counter <= 31:
      if counter == 27:
        print(counter, "\t", counter+1, "\t", counter+2, "\t", counter+3, "\t", counter+4)
        counter = counter + 7
      else:
        print(counter, "\t", counter+1, "\t", counter+2, "\t", counter+3, "\t", counter+4, "\t", counter+5, "\t", counter+6)
        counter = counter + 7
  elif value == 4:
    print("\t\t\t", counter, "\t", counter+1, "\t", counter+2, "\t", counter+3)
    counter = counter + 4
    while counter <= 31:
      if counter == 26:
        print(counter, "\t", counter+1, "\t", counter+2, "\t", counter+3, "\t", counter+4, "\t", counter+5)
        counter = counter + 7
      else:
        print(counter, "\t", counter+1, "\t", counter+2, "\t", counter+3, "\t", counter+4, "\t", counter+5, "\t", counter+6)
        counter = counter + 7
  elif value == 5:
    print("\t\t\t\t", counter, "\t", counter+1, "\t", counter+2)
    counter = counter + 3
    while counter <= 31:
      print(counter, "\t", counter+1, "\t", counter+2, "\t", counter+3, "\t", counter+4, "\t", counter+5, "\t", counter+6)
      counter = counter + 7
  elif value == 6:
    print("\t\t\t\t\t", counter, "\t", counter+1)
    counter = counter + 2
    while counter <= 31:
      if counter == 31:
        print(counter)
        counter = counter + 7
      else:
        print(counter, "\t", counter+1, "\t", counter+2, "\t", counter+3, "\t", counter+4, "\t", counter+5, "\t", counter+6)
        counter = counter + 7
  elif value == 0:
    print("\t\t\t\t\t\t", counter)
    counter = counter + 1
    while counter <= 31:
      if counter == 30:
        print(counter, "\t", counter+1)
        counter = counter + 7
      else:
        print(counter, "\t", counter+1, "\t", counter+2, "\t", counter+3, "\t", counter+4, "\t", counter+5, "\t", counter+6)
        counter = counter + 7
