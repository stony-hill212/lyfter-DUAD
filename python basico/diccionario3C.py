list_of_keys=['access_level', 'age']
employee = {
    'name': 'David',
    'email': 'dzelayasegura@gmail',
    'access_level': 5,
    'age': 27
}
for key in list_of_keys:
    employee.pop(key)
print(employee)
