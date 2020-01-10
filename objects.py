
# lets create a dictionary
month_conversion = {
    'Jan': 'January',
    'Feb': 'February',
    'Mar': 'March',
    'Apr': 'April',
    'May': 'May',
    'Jun': 'June',
    'Jul': 'July',
    'Aug': 'August',
    'Sep': 'September',
    'Oct': 'October',
    'Nov': 'November',
    'Dec': 'December'
}

print(month_conversion['Nov'])
print(month_conversion.get('Dec'))

# This will give an error: KeyError: 'abc'
# print(month_conversion['abc'])

# This will give: None
print(month_conversion.get('abc'))

# We can customize .get message if none found:
print(month_conversion.get('jan', 'Not a valid Key'))
print(month_conversion.get('Jan', 'Not a valid Key'))

# let make a function to match lower with upper case entries:
a_month = input('Enter a month name: ')
# def month_conversions(str):
#     new_month = str
#     new_month = new_month[0].upper() + new_month[1:].lower()
#     return month_conversion.get(new_month, 'Invalid entry')


# Now lets add a numbered months:
numbered_months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

def month_conversions(str):
    is_number = int(str)
    if is_number:
        return numbered_months.get(int(str), '#1.Invalid entry')
    else:
        new_month = str
        new_month = new_month[0].upper() + new_month[1:].lower()
        return month_conversion.get(new_month, '#2.Invalid entry')


print(month_conversions(a_month))

