




# employee_file = open('employees.txt', 'a') # a - for add/append
employee_file = open('index.html', 'w') # w - to create new or over write existing file
# check if it's writable
print(employee_file.writable()) # True
# write - lets add a new employee

employee_file.write('\n<h1>This is HTML file</h1>')


employee_file.close()








