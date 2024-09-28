summa = int(input('Введите сумму:'))
count1 = summa % 10
count10 = summa % 100 // 10
count100 = summa % 1000 // 100
count1000 = summa // 1000
print(f'{count1} - по 1р')
print(f'{count10} - по 10р')
print(f'{count100} - по 100р')
print(f'{count1000} - по 1000р')
