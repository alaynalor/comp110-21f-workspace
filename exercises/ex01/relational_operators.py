<<<<<<< HEAD
"""Relational Operations!"""

__author__ = "730411361"

left_input: str = input("Give me a number for the left-side. ")
right_input: str = input("Give me a number for the right-side. ")

left_number: int = int(left_input)
right_number: int = int(right_input)

less_than: str = str(left_number < right_number)
greater_or_equal: str = str(left_number >= right_number)
equal: str = str(left_number == right_number)
not_equal: str = str(left_number != right_number)

print("Left-hand side: " + left_input)
print("Right-hand side: " + right_input)
print(left_input + " < " + right_input + " is " + less_than)
print(left_input + " >= " + right_input + " is " + greater_or_equal)
print(left_input + " == " + right_input + " is " + equal)
print(left_input + " != " + right_input + " is " + not_equal)
=======
"""Demonstrates python relational operators for two number inputs."""

__author__ = "730243388"

string_one = input("Left-hand side: ")
string_two = input("Right-hand side: ")

number_one = int(string_one)
number_two = int(string_two)

print(string_one + " < " + string_two + " is " + str(number_one < number_two))
print(string_one + " >= " + string_two + " is " + str(number_one >= number_two))
print(string_one + " == " + string_two + " is " + str(number_one == number_two))
print(string_one + " != " + string_two + " is " + str(number_one != number_two))
>>>>>>> bfe00d0bc5e66cd0a568dfd7048add409d018ba1
