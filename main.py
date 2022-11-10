number_tuckets = int(input("Введите количество билетов, котороесобираетесь купить:"))
sum = 0
for i in range(number_tuckets):
    age = input("Укажите возраст посетителя:")
    age = int(age)
    if age < 18:
        print("Билет бесплатный")
    elif 25 > age >= 18:
        sum += 990
        print("Стоимость билета: 990 рублей")
    else:
        sum += 1390
        print("Стоимость билета: 1390 рублей")
if number_tuckets > 3:
    sum = sum - ((sum / 100) * 10)
    print(f"Сумма к оплате {sum} рублей с учетом 10%-ой скидки зарегистрацию на конференцию более 3-х человек:")
else:
    print(f"Сумма к оплате {sum} рублей")
