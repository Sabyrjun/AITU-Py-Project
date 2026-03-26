#Write a program that asks the user to enter a score.  If the score is 50 or higher, print You passed
# Otherwise, print You failed

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
