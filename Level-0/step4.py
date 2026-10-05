a = int(input())
b = int(input())

if a % 9 == 0 and b % 9 == 0:
    d = 9
elif a % 8 == 0 and b % 8 == 0:
    d = 8
elif a % 7 == 0 and b % 7 == 0:
    d = 7
elif a % 6 == 0 and b % 6 == 0:
    d = 6
elif a % 5 == 0 and b % 5 == 0:
    d = 5
elif a % 4 == 0 and b % 4 == 0:
    d = 4
elif a % 3 == 0 and b % 3 == 0:
    d = 3
elif a % 2 == 0 and b % 2 == 0:
    d = 2
else:
    d = 0

if d == 0:
    print("Орбиты не синхронизированы.")
else:
    print(f"Орбиты относятся как {a // d}:{b // d}.")


# line = input()

# boy = "Лев" in line
# lion = "лев" in line

# if boy and lion:
#     print('Лев, беги!')
# elif boy:
#     print('Мальчик есть, льва нет.')
# elif lion:
#     print('Есть лев, мальчика нет.')
# else:
#     print('Никого.')


# substring = input()
# s1 = input()
# s2 = input()
# s3 = input()

# print(f"{'Строка':<10}:число")

# for s in (s1, s2, s3):
#     if s == substring:
#         num = 111
#     elif substring in s:
#         num = 1
#     else:
#         num = 10
#     print(f"{s:<10}:{num:>5}")





# search = input()
# search_in = input()

# if search in search_in:
#     print('Есть!')
# else:
#     print('Спряталась.')









# quantity = int(input())
# name_offices = input()
# if quantity == 1:
#     quote = "'"
#     print(f'Черноморское отделение Арбатской конторы {quote}{name_offices}{quote}.')
# else:
#     quote = '"'
#     print(f'Черноморское отделение Арбатской конторы {quote}{name_offices}{quote}.')





# n = int(input())
# n1 = n % 2
# n2 = n % 3
# n3 = n % 4
# n4 = n % 5
# res = str(int(str(n1) + str(n2) + str(n3) + str(n4)))
# print(res)