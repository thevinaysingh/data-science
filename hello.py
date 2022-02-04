'''
print("Hello world")

a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
print("Addition of a and b is", (a+b))
'''

'''
# Numeric data type
a = 10
b = -10
c = 3.142
d = 3.000
e = 10 + 3j
f = 6j

print(a+b, c-d, e-f)
print(a-c, b-f, a*b)

s = "10010"
t = int(s)
t2 = int(s, 2)  # base 2
t10 = int(s, 10)  # base 10

print("After converting s to integer with base: %d" % t, end='\n\n')
print("After converting s to integer base 2 : %d" % t2, end='\n\n')
print("After converting s to integer base 10 : %d" % t10, end='\n\n')
'''

'''
a = float(1200.789)
b = int(5)
c = int(7)
si = round((a * b * c) / 100)
print(si)
'''

'''
val = 34527
count = 0
while val > 1:
    val /= 10
    count += 1
    print("val", val)

print("count", count)
'''

'''
# count of prime number between 2 numbers
def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n/2)+1):
        if n%i == 0:
            return False
    else:
        return True

def main():
    n1 = int(input())
    n2 = int(input())
    count = 0
    for n in range(n1, n2):
        if is_prime(n):
            count += 1
    else:
        print(count)
main()
'''

'''
# Is your Number Armstrong?
# Is number is n-narcissistic number
def main():
    value = int(input())
    count = len(str(value))
    total = 0
    for i in range(count):
        n = int(str(value)[i])
        total += n**count
    else:
        if total == value:
            print(True)
        else:
            print(False)

main()
'''

'''
# Who's the second largest?
def main():
    elements = int(input())
    input_array = input().split(' ')
    print("input_array", input_array)
    integer_array = list(map(int, input_array))
    print("integer_array", integer_array)

    largest = -1
    second_largest = -1

    for i in range(elements):
        n = integer_array[i]
        if n > largest:
            second_largest = largest
            largest = n

        if n > second_largest and n != largest:
            second_largest = n

    print(second_largest)

main()
'''

'''
# Count the uppercase and lowercase letters in a string
def is_uppercase(char):
    if char >= 'A' and char <= 'Z':
        return True
    else:
        return False


def is_lowercase(char):
    if char >= 'a' and char <= 'z':
        return True
    else:
        return False


def main():
    value = input()
    count_uppercase = len(list(filter(is_uppercase, value)))
    count_lowercase = len(list(filter(is_lowercase, value)))
    print(count_uppercase)
    print(count_lowercase)


main()
'''

'''
# Patch Up Two Matrices (100 Marks)
# For this challenge, you need to take 2 matrices as an input from the stdin , add them and print the resultant matrix to the stdout.

# Input Format
# Two matrices to be taken as an input. 
# For each matrix, on first line you need to tell that how many rows and columns your matrix need to have and these values should be separated by space. 
# Then after that, each line will represent will represent each row and you need to enter numbers which each rows should have separated by a space. 

# Constraints
# 1 <  (n,m) < 100
# 1 <  (p,q) < 100

# Output Format
# Print the resultant matrix to the stdout where each each line should represent 
# Note : Please do not include space after the numbers which are in the last column as it will affect your submission and you will not get marks. 
# each row and values in the row should be separated by a space. 

# Sample TestCase 1
# Input
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9
# 3 3
# 2 3 4
# 5 6 7
# 7 8 9
# Output
# 3 5 7
# 9 11 13
# 14 16 18
# Explanation
# Two matrices must have an equal number of rows and columns to be added. The sum of two matrices A and B will be a matrix which has the same number of rows and columns as do A and B. The sum of A and B, denoted A + B, is computed by adding corresponding elements of A and B.
def main():
    matrix_dimensions1 = input().split(' ')
    count_r1, count_l1 = list(map(int, matrix_dimensions1))
    matrix1 = list()

    for m1 in range(count_r1):
        row_input = input().split(' ')
        matrix1.append(list(map(int, row_input)))

    matrix_dimensions2 = input().split(' ')
    count_r2, count_l2 = list(map(int, matrix_dimensions2))
    matrix2 = list()

    for r in range(count_r2):
        row_input = input().split(' ')
        matrix2.append(list(map(int, row_input)))
        for c in range(count_l2):
            matrix2[r][c] += matrix1[r][c]

    for i in range(count_r2):
        print(" ".join(map(str, matrix2[i])))


main()
'''

'''
# Roll your matrix (100 Marks)
# For this challenge, you need to take a matrix as an input from the stdin , transpose it and print the resultant matrix to the stdout.

# Input Format
# A matrix is to be taken as input from stdin. On first line you need to tell that how many rows and columns your matrix need to have and these values should be separated by space. Below lines will represent the elements of the matrix where each line will represent the row of the matrix.

# Constraints
# 1 < (n,m) < 100

# Output Format
# Print the resultant matrix to the stdout where each line should represent each row and values in the row should be separated by a space.

# Sample TestCase 1
# Input
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9
# Output
# 1 4 7
# 2 5 8
# 3 6 9
# Explanation
# The transpose of a matrix is a new matrix whose rows are the columns of the original.
def main():
    matrix_dimensions1 = input().split(' ')
    row_count, col_count = list(map(int, matrix_dimensions1))
    matrix1 = list()

    for _ in range(row_count):
        row_input = input().split(' ')
        matrix1.append(list(map(int, row_input)))

    # Create an empty list in Python with certain size
    # l = [None] * 10 // List with 10 elements
    matrix2 = [[0] * row_count for _ in range(col_count)]

    for i in range(row_count):
        row = matrix1[i]
        for j in range(col_count):
            matrix2[j][i] = row[j]

    for row in matrix2:
        print(" ".join(map(str, row)))
main()
'''

'''
# Lets make a dictionary order (100 Marks)
# You need to input N words one on each line and output should be lexicographically sorted i.e the words which comes as a output should be alphabetically sorted

# Input Format
# You will be taking an integer N from STDIN.
# Following N lines contains string one on each line.

# Constraints
# 1 < N < 10000
# 1 < |S| < 1000


# Output Format
# The words should be lexicographically sorted and should be displayed one per each line.

# Sample TestCase 1
# Input
# 10
# fortran
# java
# perl
# python
# php
# javascript
# c
# cpp
# ruby
# csharp
# Output
# c
# cpp
# csharp
# fortran
# java
# javascript
# perl
# php
# python
# ruby
# Explanation
# In mathematics, the lexicographic or lexicographical order (also known as lexical order, dictionary order, alphabetical order or lexicographical product) is a generalization of the way the alphabetical order of words is based on the alphabetical order of their component letters.

def main():
    words_count = int(input())
    words = list()
    for _ in range(words_count):
        word = input()
        words.append(word)

    words.sort()
    for w in words:
        print(w)

main()
'''

'''
# Calculate power using Recursion (100 Marks)
# This program takes two integers from user ( base number and a exponent) and calculates the power. Instead of using loops to calculate power, this program uses recursion to calculate the power of a number.

# Input Format
# For this challenge, you need to take 2 integer inputs from stdin which are separated by a single space.

# Constraints
# 1 < N < 50
# 0 <= P <= 12

# Output Format
# You will print the answer to the stdout.

# Sample TestCase 1
# Input
# 4 3
# Output
# 64
# Explanation
# 4^3 = 4*4*4 = 64


def calculate_exponent(b, e):
    if e == 0:
        return 1
    elif e == 1:
        return b
    else:
        return b * calculate_exponent(b, e - 1)


def main():
    user_input = input().split(" ")
    base, exponent = list(map(int, user_input))

    total = calculate_exponent(base, exponent)

    print(total)

main()
'''

'''
# Calculate HCF or GCD
def main():
    value = input().split(' ')
    n1, n2 = list(map(int, value))

    max, min = [n1, n2] if n1 > n2 else [n2, n1]

    for n in range(min, 0, -1):
        if n1 % n == 0 and n2 % n == 0:
            print(n)
            break
main()
'''

'''
# Find pairs
def main():
    array_size = int(input())
    array_input = input().split(' ')
    array = list(map(int, array_input))
    pair_sum = int(input())
    result = False

    for i in range(array_size -1):
        item = array[i]

        if item + array[i+1] == pair_sum:
            result = True
            break
            
    print(result)

main()
'''

'''
# Find unsorted subarray in such way that if we sort the subarray then the whole array should be sorted.
def main():
    main_array_length = int('13')
    array_values = '1 2 4 7 10 11 7 12 3 7 16 18 19'.split(' ')
    array = list(map(int, array_values))
    sorted_array = sorted(array)
    subarray_start_index = 0
    subarray_end_index = main_array_length - 1

    for i in range(1, main_array_length):
        if array[i] != sorted_array[i]:
            subarray_start_index = i
            break

    for j in range(main_array_length-1, 0, -1):
        if array[j] != sorted_array[j]:
            subarray_end_index = j+1
            break

    subarray = array[subarray_start_index:subarray_end_index]

    print(" ".join(map(str, subarray)))


main()
'''

'''
# Convert binary to decimal
def main():
    binary_input = input()[::-1]
    binary_input_array = list(map(int, binary_input))
    decimal_number = 0
    for i in range(len(binary_input_array)):
        decimal_number += 2**i * binary_input_array[i]

    print(decimal_number)


main()
'''

'''
# print square of stars with space in between
def main():
    square_size = 5
    for _ in range(square_size):
        stars = ""
        for _ in range(square_size):
            stars += "* "
        print(stars.rstrip())
main()
'''

'''
# Use input() to read input from STDIN and use print to write your output to STDOUT
def main():
    no_of_elements = 6
    # no_of_elements = int(input())
    array_input = "11 22 33 44 55 66".split(' ')
    array = list(map(int, array_input))

    even_total = 0
    odd_total = 0
    for i in range(no_of_elements):
        if i % 2 == 0:
            even_total += array[i]
        else:
            odd_total += array[i]

    print(abs(even_total, odd_total))


main()
'''

'''
# play with average
def main():
    no_of_elements = int(input())
    array_input = input().split(' ')
    array = list(map(int, array_input))

    odds_array = list()
    evens_array = list()

    for i in array:
        if i % 2 == 0:
            evens_array.append(i)
        else:
            odds_array.append(i)

    total_sum = (sum(odds_array) / len(odds_array)) + (sum(evens_array) / len(evens_array))
    print(round(total_sum))

main()
'''

'''
str1 = (0xFF)

A = 1

B = 2

C = 3

print(A, end=',')

print(C, end=',')

X = A+B/C

print(int(str1))
print(type(hex(100)))
'''

'''
# Play With Average (100 Marks)
# For this challenge, you need to take number of elements as input on one line
# and array elements as an input on another line. You need to find the average of even numbers, 
# then the average of odd numbers and add them (round the averages to the nearest integers).

import math
def main():
    no_of_elements = int(input())
    array_input = input().split(' ')
    arr = list(map(int, array_input))

    even_values_array = list()
    odd_values_array = list()

    for i in arr:
        if i % 2 == 0:
            even_values_array.append(i)
        else:
            odd_values_array.append(i)

    even_average = 0 if len(even_values_array) == 0 else math.ceil(
        sum(even_values_array) / len(even_values_array))
    odd_average = 0 if len(odd_values_array) == 0 else math.ceil(
        sum(odd_values_array) / len(odd_values_array))

    addition = even_average + odd_average
    print((addition))

main()
'''

'''
# Consecutive!!! (100 Marks)
# For this challenge, you need to take number of elements as input on one line
# and array elements as an input on another line. You need to tell whether the numbers present
# in the array are consecutive or not.
def main():
    no_of_elements = int(input())
    array_input = input().split(' ')
    arr = list(map(int, array_input))
    arr.sort()
    result = True
    for i in range(1, len(arr)):
        if not(arr[i] - arr[i-1] == 1):
            result = False
            break

    print(result)

main()
'''

'''
# Biggest Digit In A Number (100 Marks)
# For this challenge, you will take an integer input from stdin, store it in a variable,
# find the digits in a number and then print the biggest of them.
def main():
    value = input()

    digits_array = [int(char) for char in value]
    print(max(digits_array))


main()
'''

'''
# Play with digits
def main():
    value = input()
    digits_array = [int(char) for char in value]

    even = sum([i for i in digits_array if i % 2 == 0])
    odd = sum([i for i in digits_array if i % 2 != 0])

    print(abs(even-odd))

main()
'''

'''
# Compare two numbers (100 Marks)
# For this challenge, you will take two integers input from stdin,
# sum the digits of a number and same is to be done with another number.
# Then compare the sum of the digits of two numbers and if one sum found to be greater
# then print that number to the stdout. If found both sum to be equal then print 'Equal'
# to the stdout.


def main():
    values = input().split()

    sum1 = sum([int(char) for char in values[0]])
    sum2 = sum([int(char) for char in values[1]])

    if sum1 > sum2:
        print(values[0])
    elif sum2 > sum1:
        print(values[1])
    else:
        print("Equal")

main()
'''

'''
def main():
    rox_col_input = input().split()
    rows, cols = list(map(int, rox_col_input))

    diagonal1 = list()
    diagonal2 = list()

    for r in range(rows):
        row_input = input().split()
        row = list(map(int, row_input))
        diagonal1.append(row[r])
        diagonal2.append(row[rows - 1 - r])

    diagonal1_sum = sum(diagonal1)
    diagonal2_sum = sum(diagonal2)

    if diagonal1_sum == diagonal2_sum:
        print("Equal")
    elif diagonal1_sum > diagonal2_sum:
        print("Diagonal1")
    else:
        print("Diagonal2")


main()
'''

'''
# Which row is bigger?
def main():
    rox_col_input = input().split()
    rows, cols = list(map(int, rox_col_input))

    rows_sum = list()

    for r in range(rows):
        row_input = input().split()
        row = list(map(int, row_input))
        rows_sum.append(sum(row))
    
    max_value = max(rows_sum)
    max_arrays = list()
    for i in range(len(rows_sum)):
        if rows_sum[i] == max_value:
            max_arrays.append(i)

    if len(max_arrays) == len(rows_sum):
        print('Equal')
    else:
        print(f'Row {max_arrays[0] + 1}')

main()
'''

# a = 10
# b = 12
# print(10 & 12)


# def user(name, age):
#     print(name, age)


# user("vinay", 23)
# user(name="vinay", age=23)
# user("vinay", age=23)

# arr = [12, 13, 14]
# print(arr[-1])

s = "()[]{}"

length_s = len(s)

for i in range(0, length_s, 2):
    print(s[i], s[i+1], ":", s[i] == s[i+1])
