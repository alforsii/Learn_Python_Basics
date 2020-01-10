

try:
    employee_file = open('employees.txt', 'r') # 'r' - read
    # 1.to check if file is readable
    print(employee_file.readable()) # True
    # 2.to read
    # print(employee_file.read())   # read all

    # 3.read line (will read first line and so on)
    # print(employee_file.readline()) # line 1
    # print(employee_file.readline()) # line 2
    # print(employee_file.readline()) # line 3

    # 4.read lines - will store in array and each line wil be each index of an array
    # print(employee_file.readlines())

    # 5. now we can get any specific line
    # print(employee_file.readlines()[3])

    # 6. also we can loop trough employee_file.readlines()
    for employee in employee_file.readlines():
        print(employee)

    employee_file.close()
except FileNotFoundError as err:
    print(err)
