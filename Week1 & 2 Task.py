
# TYPES OF VARIABLES
name = "Alan Raj"  
age = 25
height = 5.8

print(name, type(name))
print(age, type(age))
print(height, type(height))


#LIST
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[0], fruits[-1])

fruits.append("orange")
print(fruits)

fruits.pop(1)
print(fruits)

fruits.sort()
print(fruits)


#TUPLES
languages = ("Python", "Java", "C++")
print(languages[1])

languages_list = list(languages)
languages_list[1] = "JavaScript"
languages = tuple(languages_list)
print(languages)


# Data Dictionary - Basics
student = {"name": "John", "age": 18, "grade": "A"}
print(student["grade"])

student["hobby"] = "reading"
print(student)

del student["age"]
print(student)


# Data Dictionary - Operations
marks = {"Math": 85, "Science": 90, "English": 78}
average = sum(marks.values()) / len(marks)
print(average)

marks["Math"] = 88
print(marks)
print("History" in marks)


#Functions - Basics

def square(n):
    return n * n
print(square(7))


#Functions - Default Arguments

def greet(name, message="Welcome!"):
    print(f"{message}, {name}!")
greet("Alan", "Hello")
greet("Raj")


#Functions - Positional and Keyword Arguments

def student_info(name, age, grade="A"):
    print(f"Name: {name}, Age: {age}, Grade: {grade}")

student_info("Alan", 27, "B")

student_info(name="Raj" , grade="C", age=25)


#Lists and Functions

numbers = [10, 20, 30, 40, 50]

def double_values(lst):
    return [num * 2 for num in lst]
new_numbers = double_values(numbers)
print(new_numbers)


#Combining Data Dictionary and Functions

students = {"Alice": 85, "Bob": 78, "Eve": 92}

def add_student(student_dict, name, grade):
    student_dict[name] = grade

def average_grade(student_dict):
    return sum(student_dict.values()) / len(student_dict)

add_student(students, "David", 88)
print(students)

print(average_grade(students))


#Variables and Data Types

a = 5
b = 10
a, b = b, a  
print(a, b) 


#Lists - Nested Lists

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(data[1][1]) 

flat_list = sum(data, [])
print(flat_list)


#Dictionary - Complex Keys

coordinates = {(1, 2): 3, (3, 4): 7, (5, 6): 11}

def get_sum(coord_dict, x, y):
    return coord_dict.get((x, y))
print(get_sum(coordinates, 3, 4)) 


#Functions - Nested Functions

def outer_function(a, b):
    def inner_function(x, y):
        return x**2 + y**2
    return inner_function(a, b)
print(outer_function(3, 4)) 


#Functions - Lambda & Map

numbers = [1, 2, 3, 4, 5]
cubed_numbers = list(map(lambda x: x**3, numbers))
print(cubed_numbers)


#Functions - Recursion

def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)
print(sum_of_digits(1234)) 


#List Comprehensions

numbers = [x for x in range(1, 101) if x % 5 == 0 and x % 3 != 0]
print(numbers)


#Dictionary - Sorting by Values######

scores = {"Alice": 90, "Bob": 85, "Eve": 92}
sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print(sorted_scores) 


#Sets - Unique Characters

def unique_chars(s):
    unique_set = set(s)
    return unique_set, len(unique_set)
print(unique_chars("hello")) 


#Tuples - Finding Common Elements

t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7, 8)
common_elements = set(t1) & set(t2)
print(common_elements)


#Dictionary - Reverse Key-Value Mapping

data = {"A": 1, "B": 2, "C": 3}
reversed_data = {v: k for k, v in data.items()}
print(reversed_data) 


#Functions - Multiple Return Values

def math_operations(a, b):
    return a+b, a-b, a*b, a/b
print(math_operations(10, 2))


#List - Finding Second Largest Number

def second_largest(lst):
    first = second = float('-inf')
    for num in lst:
        if num > first:
            second, first = first, num
        elif num > second and num != first:
            second = num
    return second
print(second_largest([10, 20, 4, 45, 99]))


#List - Pair Sum Problem

def find_pairs(lst, target):
    pairs = []
    for i in range(len(lst)): 
        for j in range(i + 1, len(lst)):  
            if lst[i] + lst[j] == target:  
                pairs.append((lst[i], lst[j])) 
    return pairs
print(find_pairs([2, 4, 3, 7, 1, 9], 10))






















