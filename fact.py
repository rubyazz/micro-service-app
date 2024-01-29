# def fact(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return num * fact(num - 1)


# print(fact(50))


# def pali(w, first, last):
#     if w[first] != w[last]:
#         return False
#     elif last <= first:
#         return True
#     else:
#         return pali(w, first + 1, last - 1)


# word = input()

# first = 0
# last = len(word) - 1

# print(pali(word, first, last))


# selection sort

# arr = [2, 45, 12, 8]

# for i in range(len(arr)):
#     mini = arr[i]
#     for j in range(i + 1):
#         if arr[i] < arr[j]:
#             mini = j
#             arr[j], arr[i] = arr[i], arr[j]
# print(arr)


# mishka i starshi brat

# l = int(input())
# b = int(input())
# k = 0

# while l <= b:
#     k = k + 1
#     l = l * 3
#     b = b * 2

# print(k)


# B. Красивый год
# a = input()

# a = int(a) + 1

# b = set(str(a))

# while len(set(b)) != 4:
#     a = int(a) + 1
#     b = set(str(a))

# print(a)

# C. Аукцион второй цены
# members = int(input())
# money = 0
# x = [int(x) for x in input().split()]

# for i in range(x):
#     if money == x:
#         print(members, money)

# return members, money

# H. Перевод

# s = input()
# t = input()

# reversed_one = t[::-1]

# if s == reversed_one:
#     print("YES")
# else:
#     print("NO")

# G. Цветные камешки (упрощ. редакция)

# s = input()
# t = input()


# counter = 0

# for i in range(len(t)):
#     if counter < len(s) and s[counter] == t[i]:
#         counter = counter + 1

# print(counter + 1)

# buble sort
# buble sort


# def swap(a, b, massive):
#     massive[a], massive[b] = massive[b], massive[a]


# def buble(arr):
#     for i in range(len(arr)):
#         for j in range(i):
#             if arr[i] < arr[j]:
#                 swap(i, j, arr)
#     return arr


# array = [12, 5, 1523, 15, -54, -5, 0, 45555]

# print(buble(array))

# A. Петя и книга

# gen_page = int(input())

# pages_for_days = [15, 20, 20, 15, 10, 30, 45]
# count = 0

# for i in range(len(pages_for_days)):
#     i = i + 1
#     count = count + i
#     if count == gen_page:
#         print(count)
#         break;


# B. Открытки и фотографии

# n = input()
# temp = ''
# i = 0
# counter = 0

# while len(n) > 0:
#     if len(temp) == 0:
#         temp += n[0]
#         if len(n) > 1:
#             n = n[1:]
#         else:
#             n = ''
#     elif len(temp) > 0 and len(temp) < 5:
#         if n[0] in temp:
#             temp += n[0]
#             if len(n) > 1:
#                 n = n[1:]
#             else:
#                 n = ''
#         else:
#             temp = ''
#             counter += 1
#     elif len(temp) >= 5:
#         counter += 1
#         temp = ''

# if len(n) == 0:
#     counter += 1

# print(counter)


# D. cAPS lOCK

word = input()
result = ""

if word.islower() or (word[0].isupper() and word[1:].islower()):
    result = word
elif len(word) and word.islower() == 1:
    result = word.upper()
elif len(word) and word.isupper() == 1:
    result = word.lower()
else:
    for letter in word:
        if letter.isupper():
            result += letter.lower()
        else:
            result += letter.upper()
print(result)
