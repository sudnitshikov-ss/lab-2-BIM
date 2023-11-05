money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month = 0  # количество месяцев, которое можно прожить
sum = money_capital - spend
while sum > 0:
    sum = sum + salary - spend
    spend = (1+increase)*spend
    month += 1

print("Количество месяцев, которое можно протянуть без долгов:", month)
