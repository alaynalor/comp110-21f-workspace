<<<<<<< HEAD
"""Numeric Operations!"""

__author__ = "730411361"

left_input: str = input("Give me a number for the left-side. ")
right_input: str = input("Give me a number for the right-side. ")

left_number: int = int(left_input)
right_number: int = int(right_input)

exponent_answer: str = str(left_number ** right_number)
division_answer: str = str(left_number / right_number)
integer_division_answer: str = str(left_number // right_number)
remainder_answer: str = str(left_number % right_number)

print("Left-hand side: " + left_input)
print("Right-hand side: " + right_input)
print(left_input + " ** " + right_input + " is " + exponent_answer)
print(left_input + " / " + right_input + " is " + division_answer)
print(left_input + " // " + right_input + " is " + integer_division_answer)
print(left_input + " % " + right_input + " is " + remainder_answer)
=======
"""Demonstrates python numeric operators for two input numbers."""

__author__ = "730243388"

string_one = input("Left-hand side: ")
string_two = input("Right-hand side: ")

number_one = int(string_one)
number_two = int(string_two)

print(string_one + " ** " + string_two + " is " + str(number_one ** number_two))
print(string_one + " / " + string_two + " is " + str(number_one / number_two))
print(string_one + " // " + string_two + " is " + str(number_one // number_two))
print(string_one + " % " + string_two + " is " + str(number_one % number_two))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
