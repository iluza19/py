
n1 = int(input("Введите первые 3 цифры в билете: ")) 
n2 = int(input("Введите последние 3 цифры в билете: ")) 
a1=n1//100+(n1-n1//100*100)//10+n1%10
a2=n2//100+(n2-n2//100*100)//10+n2%10
if a1==a2:
    print("билет счастливый")
else:
    print("билет не счастливый")