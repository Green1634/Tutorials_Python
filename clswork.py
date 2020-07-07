#Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user
# print('enter any number')
# number = int(input())
# if number % 2 == 0: 
#     print('number is even')
# if number % 3 == 0:
#     print('number is odd')

# #Write a Python program to count the number 4 in a given list. Say the list is [5,8,4,4,0,5,4,11,8,4]
# Number = [5,8,4,4,0,5,4,11,8]
# y = 0
# for x in Number:
#     if x == 4:
#         y = y + 1
# print('the number of 4 in this list is', y)

# #Write a python program that accepts two inputs from user, add the numbers and print the result
# print('enter the first number')
# number1 = int(input())
# print('enter the second number')
# number2 = int(input())
# print('the number is', number1 + number2)
# if number1 > number2: 
#     print('the greatest number is', number1)
# elif number2 > number1:
#     print('the greatest number is', number2)

#Write a Python program that will accept the base and height of a triangle and compute the area
# print('enter the base of the triangle')
# base = int(input())
# print('enter the height of the triangle')
# height = int(input())
# Area = height*base/2
# # print('the area of the triangle is', Area)

# #Design a simple calculator for a user. The calculator should be able to add, subtract, divide, multiply, and find square root of a number
# import math
# operations = ['a', 's', 'd', 'm', 'sq']
# for operation in operations: 
#     a = 'addition'
#     s = 'subtract'
#     d = 'divide'
#     m = 'multiply'
#     sq = 'sqroot'
# print('what operation do you want to perform, to add enter a, to substract enter s, to divide enter d, to multiply enter m, and to find the square root enter sq')
# operation = str(input ())

# if operation == 'sq':
#     print('enter the squarenumber')
#     squarenumber = int(input())
#     squarenumber = math.sqrt(squarenumber)
#     print('the square number', squarenumber)
# elif operation == 's':
#     print ('enter the first number')
#     first_number = int(input())
#     print ('enter the second nuber')
#     second_number = int(input())
#     print ('the ans is', first_number - second_number) 
# elif operation == 'd': 
#     print ('enter the first number')
#     first_number = int(input())
#     print ('enter the second nuber')
#     second_number = int(input())
#     print ('the ans is', first_number / second_number) 
# elif operation == 'm':
#     print ('enter the first number')
#     first_number = int(input())
#     print ('enter the second nuber')
#     second_number = int(input())
#     print ('the ans is', first_number * second_number) 
# elif operation == 'a':
#     print ('enter the first number')
#     first_number = int(input())
#     print ('enter the second nuber')
#     second_number = int(input())

#     print ('the ans is', first_number + second_number) 

    # x = math.sqrt(input()
    # print('the square root is', x)

# Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence. Go to the editor
# Sample numbers list :
# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527

# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527]
# for x in numbers: 
#     if x % 2 == 0 and x <237:
#         print(x)

# #Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20
# print ('input the first number')
# Number_1 = int(input())
# print ('input the second number')
# Number_2 = int(input())
# Sum = Number_1 + Number_2
# if Sum >= 15 and Sum <=20:
#     print(20)

#given a list of numbers for example [2,4,8,10,1,14,15,3,0,5] write a python program that return the position of a number from the user in the list 
List = [2,4,8,10,1,14,15,3,0,5]
numbers = List
while (1):
    position = 1
    print ('guess any number in my list')
    number = int(input())
    if number in List:
        print('correct')
    elif number not in List:
        print('wrong')
        exit()
    for x in List:
        if x == number:
            print('the position of the number is', position)
            break
        else: 
            position = position + 1