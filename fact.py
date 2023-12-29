def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)


print(fact(50))


def pali(w, first, last):
    if w[first] != w[last]:
        return False
    elif last <= first:
        return True
    else:
        return pali(w, first + 1, last - 1)


word = input()

first = 0
last = len(word) - 1

print(pali(word, first, last))
