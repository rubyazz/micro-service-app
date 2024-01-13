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


# def buble_sort(list):
#     for i in range(len(arr)):
#         for j in range(i):
#             if arr[i] < arr[j]:
#                 arr[i], arr[j] = arr[j], arr[i]
#     return arr


# arr = [8888, -451, 1, 45, 2, 0, 54, 4545, -45, 62, 15]

# print(buble_sort(arr))


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
members = int(input())
money = 0
x = [int(x) for x in input().split()]

for i in range(x):
    if money == x:
        print(members, money)

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
