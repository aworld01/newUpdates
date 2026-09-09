from datetime import datetime
from dateutil.relativedelta import relativedelta

# Take input from user
date1 = input("Enter 1st date (DD-MM-YYYY): ")

date2 = input("Enter 2nd date (DD-MM-YYYY): ")

# Convert to date objects
d1 = datetime.strptime(date1, "%d-%m-%Y")

d2 = datetime.strptime(date2, "%d-%m-%Y")

# Calculate difference
diff = relativedelta(d2, d1)

# Absolute values (optional)
years = abs(diff.years)
months = abs(diff.months)
days = abs(diff.days)

print(f"Difference: {years} years, {months} months, {days} days")