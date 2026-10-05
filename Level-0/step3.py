n = int(input())
if n % 3 == 0:
   n = n // 3
elif n % 2 == 0:
   n = n // 2
else:
   n = n - 1
print(n)





# n = int(input())

# d1 = n // 1000
# d2 = (n // 100) % 10
# d3 = (n // 10) % 10
# d4 = n % 10
# summa = d1 + d2 + d3 + d4

# flag = False

# if summa % d1 == 0:
#     print('Сумма цифр', n, 'делится на', d1)
#     flag = True
# if summa % d2 == 0:
#     print('Сумма цифр', n, 'делится на', d2)
#     flag = True
# if summa % d3 == 0:
#     print('Сумма цифр', n, 'делится на', d3)
#     flag = True
# if summa % d4 == 0:
#     print('Сумма цифр', n, 'делится на', d4)
#     flag = True

# if not flag:
#     print('Сумма цифр', n, 'не делится на свои цифры.')







# num = int(input())
# root = num ** 0.5
# if root == int(root):
#     print('Квадрат')
# else:
#     print('Не квадрат')

# humidity = int(input())
# if humidity < 30:
#     print('Сухо')
# elif humidity > 70:
#     print('Влажно')
# else:
#     print('Нормально')