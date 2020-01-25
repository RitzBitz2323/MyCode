def factorial(number):
    if number >= 1:
        return number*factorial(number-1)
    else:
        return 1

# #    index = number
# #    factorial = 1
#     while(index > 0):
#         factorial = factorial*index
#         index = index - 1
#     print(factorial)

print("Factorial Program")
num = int(input("Input a number you want the factorial of: "))
print(factorial(num))
