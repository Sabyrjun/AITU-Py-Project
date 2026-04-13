'''
#1
nums = list(map(int, input("Введите числа через пробел: ").split()))

if len(nums) < 2:
    print("Нужно как минимум два числа")
else:
    max1 = max2 = float('-inf')

    for n in nums:
        if n > max1:
            max2 = max1
            max1 = n
        elif n > max2 and n != max1:
            max2 = n

    print("Второй по величине элемент:", max2)
'''

'''
#2
L = [1, 2, 3, 4, 5]

rotated_L = [L[-1]] + L[:-1]

print(rotated_L)
'''

'''
#3
nums = list(map(int, input("Введите числа списка: ").split()))

even_list = []
odd_list = []

for n in nums:
    if n % 2 == 0:
        even_list.append(n)
    else:
        odd_list.append(n)

print("Четные:", even_list)
print("Нечетные:", odd_list)
'''

'''
#4
L = [[1, 2], [3, 4], [5]]
flat_list = []

for sublist in L:
    for item in sublist:
        flat_list.append(item)

print(flat_list)
'''

'''
#5
t = (1, 2, 2, 3, 2, 4)
count_2 = t.count(2)
print("Число 2 встречается:", count_2, "раза")
'''

'''
#6
t = (1, 2, 3)
temp_list = list(t)
temp_list.append(4)
t_modified = tuple(temp_list)
print(t_modified)
'''

'''
#7
t = (10, 20, 30)
a, b, c = t
print("a =", a)
print("b =", b)
print("c =", c)
'''

'''
#8
t = ((1, 5), (2, 3), (7, 1))
max_tuple = max(t, key=sum)
print("Кортеж с наибольшей суммой:", max_tuple)
'''

'''
#9
user_input = input("Введите числа через пробел: ")
nums = list(map(int, user_input.split()))
unique_nums = list(set(nums))
print("Уникальные числа:", unique_nums)
'''

'''
#10
A = {1, 2}
B = {1, 2, 3, 4}
is_subset = A.issubset(B)
print("A является подмножеством B:", is_subset)
'''

'''
#11
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
sym_diff = set1 ^ set2
print("Симметричная разность:", sym_diff)
'''

'''
#12
word = "programming"
unique_chars = set(word)
print("Уникальные символы:", unique_chars)
'''
'''
#13
L = [2, 7, 11, 15]
target = 9
for i in range(len(L)):
    for j in range(i + 1, len(L)):
        if L[i] + L[j] == target:
            print("Найдены числа:", L[i], "и", L[j])
'''

'''
#14
L = [1, 2, 2, 3, 4, 4, 5]
unique_elements = [x for x in L if L.count(x) == 1]
print(unique_elements)
'''

'''
#15
L1 = [1, 2, 3, 4]
L2 = [2, 3, 5]
L3 = [2, 3, 6]
common_elements = list(set(L1) & set(L2) & set(L3))
print(common_elements)
'''






