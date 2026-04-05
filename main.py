#Write a program that asks the user to enter a score.  If the score is 50 or higher, print You passed
# Otherwise, print You failed
"""
a = int(input())
if a <= 50:
    print("You pass")
else:
    print("You fail")


#Write a program that asks the user to enter a day of the week.  If the day is Saturday or Sunday, print Weekend
# Otherwise, print Weekday

a = input()
if a == 'Saturday' or a == 'Sunday':
    print("Weekend")
else:
    print("Weekday")


#Task 3. Numbers from 1 to 5
#Use a while loop to print numbers from 1 to 5.

a = 0
while a < 5:
    print(a+1)
    a += 1

a = input()
b = len(a)
for i in range(b):
    print(a[i])


#Task 5. Uppercase and Lowercase
#Ask the user to enter a word.
#Print:  the word in uppercase  the word in lowercase


a = input()
b = a.upper()
c = a.lower()
print(b, c, sep='\n')




nums = [1, 2, 3, 4, 5]
print(nums[1])
nums.append(10)

a = [1, 2, 3, 4, 5]
print(a[:3])
print(a[-2:])
print(3 in a)

print(list(set([1, 2, 2, 3, 4, 4])))
A = {1, 2, 3}
B = {2, 3, 4}
print(A & B)

d = {"name": "Ali", "age": 20}
d["city"] = "Astana"
print(d["name"])
"""
from os.path import sep

"""
#task 1
a = int(input())
b = int(input())
if a < b:
    c = a
    a = b
    b = c
    print(a-b)
else:
    print(a-b)
"""

"""
#task 2

a=int(input())
for i in range(0, a+1, 2):
    print(i, end=" ")
"""

"""
#task 3
a = int(input())
for i in range(a, -1, -1):
    print(i, end=" ")
"""
"""
#task 4
a = int(input())
if a > 500:
    print("TOTAL: ", a*0.9,  "USD Thank you!")
else:
    print("No discount")
"""

"""
#task 5
a = input()
b = int(a[0])+int(a[1])+int(a[2])
c = int(a[3])+int(a[4])+int(a[5])
if b == c:
    print("Yes")
else:
    print("No")
"""

"""
#task 6
D, t1, t2 = map(int, input().split())
v1 = 15/t1
v2 = (D - 15)/t2
if v1 > v2:
    print("before")
else:
    print("after")
"""

'''
#task 7
a = 1
sum = 0
counter = 0

while a == 1:
    b = int(input())
    if b == 0:
        break
    sum += b
    counter += 1
avg = sum/counter
print(sum, avg, sep='\n')
'''

'''
#task 8
a = 1
max = 0
min = 0

while a == 1:
    b = int(input())
    if b == 0:
        break
    if b >= max:
        max = b
    if b <= min:
        min = b
print(max, min, sep='\n')
'''

'''
#task 9
a = 1
odd = 0
while a == 1:
    b = int(input())
    if b == 0:
        break
    if b%2 == 1:
        sum += b
print(sum)
'''

'''
#task 10
a = 1
sum = 0
counter = 0
max = None
min = None
odd = 0

while a == 1:
    b = int(input())
    if b == 0:
        break
    sum += b
    counter += 1
    if max is None or b > max:
        max = b
    if min is None or b < min:
        min = b
    if b % 2 == 1:
        odd += b
avg = sum/counter
print('Sum: ', sum, '\n' 'Avg: ', avg, '\n' 'Min: ', min, '\n' 'Max: ', max, '\n' 'Odd sum: ', odd)
'''




























