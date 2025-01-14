from datetime import datetime
current_year = datetime.now().year

current_year %= 2000
birth_year = 2000

number = 4

number *= 2
number += 5
number *= 50
number += 1749
number += current_year
number -= birth_year

print (number)
