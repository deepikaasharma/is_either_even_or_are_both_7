"""Complete the is_either_even_or_are_both_7 function below.

is_either_even_or_are_both_7 takes two numbers as parameters, and returns True if either number is even, or, if both numbers are 7. Otherwise it returns False.

output = is_either_even_or_are_both_7(3, 7)
print(output) # --> False

output = is_either_even_or_are_both_7(2, 3)
print(output) # --> True

"""
def is_either_even_or_are_both_7(num1, num2):
  if num1%2==0 or num2%2==0:
    return True
  elif num1==7 and num2==7:
    return True
  else:
    return False

output=is_either_even_or_are_both_7(9,7)
print(output)


