variable_outside_function_scope=157

def print_variable():
  print(f'Inside function:{variable_outside_function_scope}')


print_variable()
print(f'Outside function:{variable_outside_function_scope}')


variable_outside_function_scope="BJJ"

def print_variable():
  print(f'Inside function: {variable_outside_function_scope}')


print_variable()
print(f'Outside function: {variable_outside_function_scope}')