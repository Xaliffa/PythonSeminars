year_number = int(input('Enter the number of year: '))
if year_number % 400 == 0 or (year_number % 4 == 0 and year_number % 100 != 0):
    print('YES')
else:
    print('NO')

