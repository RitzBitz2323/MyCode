def factorial(number):
    count = 0
    index = number
    factorial = 1
    while(count < 8 and index > 0):
        factorial = factorial*index
        index = index - 1
        count = count + 1
    print(factorial)

print("Factorial Program")
num = int(input("Input a number you want the factorial of: "))
factorial(num)