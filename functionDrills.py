'''
@author: amayamunoz
'''

'''
For this assignment you should read the task, then below the task do what it asks you to do.For tasks with return statements, you can test out if you are correct by calling the function and printing what is returned
EXAMPLE TASK:
'''
#EX) Define a function that adds two numbers and returns the result
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers
'''
END OF EXAMPLE
'''

'''
START HERE
'''
#1) Define a function that subtracts the second number from the first number. Return the result.
def subtract_two_numbers(num1, num2):
    difference = num1 - num2
    return difference

#2) Define a function that divides a number by 2, multiplies it by 77, and then adds 10000. Return the result.
def number_manipulation(num):
    manipulatedNumber = (num * 2 * 77) + 10000
    return manipulatedNumber

#3) Define a function that checks if two numbers are equal. If they are equal, return true. If they are not equal, return false.
def num_equal_check(num1, num2):
    equal = (num1 == num2)
    return equal

#4) Define a function that takes in two numbers and returns the larger number. If they are the same, it should just return that number.
def larger_num(num1, num2):
    if num1 >= num2:
        largerNum = num1
    else:
        largerNum = num2
    return largerNum

#5) Define a function that takes in two words and returns a string that contains both words combined.
def combine_words(word1, word2):
    combinedString = word1 + word2
    return combinedString

#6) Define a function that takes in three numbers. If the first number is equal to the second OR the third number, return true. Else, return false.
def numbers_equal_check(num1, num2, num3):
    equal = (num1 == num2 or num1 == num3)
    return equal

#7) Define a function that prints your name.
def my_name():
    print("Ethan")

#8) Define a function that takes in a string that is the name of a color. If that string is equal to your favorite color, it prints "That's my favorite color!" If itis not, it prints "That is not my favorite color. Try again."
def my_favorite_color(color):
    if color == "blue":
        print("That's my favorite color!")
    else:
        print("That is not my favorite color. Try again.")

#9) Define a function that takes in a number. If the number is not equal to zero, the function runs a loop until the number reaches 0. HINT: Within the loop, keep subtracting 1 from the number.
def make_num_zero(num):
    if num != 0:
        while num != 0:
            num -= num

'''YOUR OWN FUNCTION'''
#10) Create your own function that solves any problem you can think of
#This function removes all vowels from a given string, besides y, and returns it
def remove_vowels(voweledString):
    vowels = ['a', 'e', 'i', 'o', 'u']
    i = 0
    devoweledString = voweledString
    while i < len(devoweledString):
        if devoweledString[i] in vowels:
            devoweledString = devoweledString[0:i] + devoweledString[(i+1):len(devoweledString)]
            i -= 1
        i += 1
    return devoweledString