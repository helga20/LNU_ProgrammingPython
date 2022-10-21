number = int(input('Введіть N: '))
copy_number = number
digit_sum  = 0
while number > 0 :
    digit_sum +=  number%10
    number = number//10
if copy_number%digit_sum == 0 :
    print('harshad')
else:
    print('NOT harshad')
    

