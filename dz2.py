#Найти сумму чисел списка стоящих на нечетной позиции
#Пример:[1,2,3,4] -> 4
nums = [1,2,3,4]
sum = 0
for i in range(0, len(nums), 2):
    sum += nums[i]
print(sum)

#Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
#Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 
nums = [2, 3, 4, 5, 6]
for i in range(0, round(len(nums) / 2 + len(nums) % 2)):
    nums[i] *= nums[ -1 - i]
print(nums[:len(nums) // 2 + len(nums) % 2])

#В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов. 
#Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
nums = [1.1, 1.2, 3.1, 5, 10.01]
min_num = 1
for i in range (0, len(nums)):
    nums[i] -= round(nums[i])
    if nums[i] != 0 and nums[i] < min_num:
        min_num = nums[i]
result = max(nums) - min_num
print(round(result, 2))

#Написать программу преобразования десятичного числа в двоичное
n10 = int(input('Введите число: '))
print(bin(n10)[2::])