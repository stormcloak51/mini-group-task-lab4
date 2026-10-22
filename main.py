month = int(input("Введите номер месяца (1-12): "))
<<<<<<< HEAD
if month == 12 or month == 1 or month == 2:
    print("Зима")
elif month == 3 or month == 4 or month == 5:
    print("Весна")
elif month == 6 or month == 7 or month == 8:
    print("Лето")
elif month == 9 or month == 10 or month == 11:
    print("Осень")
else:
    print("Некорректный номер месяца! Введите число от 1 до 12.")
=======

match month:
    case 12 | 1 | 2:
        print("Зима")
    case 3 | 4 | 5:
        print("Весна")
    case 6 | 7 | 8:
        print("Лето")
    case 9 | 10 | 11:
        print("Осень")
    case _:
        print("Некорректный месяц")
>>>>>>> grisha
