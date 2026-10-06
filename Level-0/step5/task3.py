num_one = int(input())
num_two = int(input())
num_three = int(input())

result = (
    num_one % 7 == num_two // 2 or
    num_one % 7 == num_three // 2 or
    num_two % 7 == num_one // 2 or
    num_two % 7 == num_three // 2 or
    num_three % 7 == num_one // 2 or
    num_three % 7 == num_two // 2
)

print(result)

# Для трёх введённых чисел определите, есть ли среди них такая пара, что остаток от деления 
# на 7 одного числа равен целой части от деления на 2 другого числа? 
# Если такая пара есть, выведите True, если нет, то False.

