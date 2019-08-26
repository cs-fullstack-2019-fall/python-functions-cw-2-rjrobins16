# # python-functions-cw_2
# 
# 
# ### Problem 1:
# Create a function that will ask the user for a number.
#     Use the function to get two numbers from the user, then pass the two numbers to a function.
#     Add, subtract, multiple, and divide the numbers.



def function1():
    userNumber = int(input("Enter a number."))
    return userNumber

def function2(number1,number2):
    print(number2 + number1)
    print (number2 - number1)
    print (number2 * number1)
    print (number2/number1)


function2(function1(), function1())

    