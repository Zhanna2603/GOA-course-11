"""3) კომენტარებით აღზერე ცვლადის შექმნის თითოეული ნაბიჯი(სულ 3)"""
# Хороший код документируется
print("Изучите Python шаг за шагом!")

# Создадим список месяцев
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                'Jul','Aug','Sep','Oct','Nov','Dec']

# Функция вывода календарных месяцев
def showCalender(months):
    # Цикл for проходит по списку и вводит название каждого месяца
    for month in months:
        print(month)

showCalender(months)