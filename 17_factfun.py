def factorial(n):
  if n < 0:
    print("Factorial of a negative number is undefined.")
  elif n == 0:
    return 1
  else:
    return n * factorial(n - 1)


num = int(input("Enter the number to find factorial"))
factorial_of_n = factorial(num)
print(factorial_of_n)
