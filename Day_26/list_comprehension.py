# region intro to list comprehension

numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]
print(new_list)
# endregion

# region list comprehension for strings with if statement

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

new_list = [name.upper() for name in names if len(name) > 5]

print(new_list)
# endregion

# region Exercise - square numbers in a list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [num * num for num in numbers]

print(squared_numbers)
# endregion

# region Exercise - filter even number from a list
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)
# endregion


numbers = [1, 2, 3, 4, 5, 6]
new_list = [num for num in numbers if num % 2 == 0]
for number in numbers:
    if number % 2 == 0:
        new_list.append(number)
