import company
import transport
import worker
import order
import datetime
import logging

logging.basicConfig(filename="log.log", level=logging.INFO, format=
                    "%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s")
logging.debug("This is a debug message")
logging.info("This is an info message")
logging.warning("This is a warning")
logging.error("This is an error message")
logging.critical("FATAL!!!")
log = logging.getLogger("mainLogger")


def main() -> None:
    this_company = company.Company()
    while True:
        switch = input("Меню:\n(1)Управление сотрудниками\n(2)Управление транспортом\n"
                       "(3)Управление заказами\n(4)Просмотр информации\n(5)Выйти\n")
        if switch == "1":
            worker_control(this_company)
            continue
        if switch == "2":
            transport_control(this_company)
            continue
        if switch == "3":
            order_control(this_company)
            continue
        if switch == "4":
            view_info(this_company)
            continue
        if switch == "5":
            return
        else:
            print("Неправильный ввод!")
            input("Нажмите Enter для продолжения!")
            continue


def worker_control(this_company: company.Company) -> None:
    while True:
        switch = input("(1)Нанять сотрудника\n(2)Уволить сотрудника\n(3)Назначить на новую должность\n"
                       "(4)Просмотр вакансий\n(5)Добавление вакансий\n(6)Удаление вакансий\n(7)Поиск сотрудника\n"
                       "(8)Список всех сотрудников\n(9)Сортировать\n"
                       "(10)Вывести всех у кого день рождения в этом месяце\n(11)Назад\n")
        if switch == "1":
            while True:
                try:
                    name = input("Введите имя:\n")
                    position = input("Введите должность"
                                     "(При наличии данной вакансии она будет занята этим сотрудником):\n")
                    birthday = list(map(int, input("Введите день рождения в формате (2017.4.18):").split(".")))
                    salary = int(input("Введите зарплату сотрудника:"))
                    this_company.add_new_worker(
                        worker.Worker(name, position, datetime.date(birthday[0], birthday[1], birthday[2]), salary))
                except ValueError:
                    log.exception("Неправильный ввод!")
                    print("Неправильный ввод!\n")
                    continue
                except TypeError:
                    log.exception("Преобразование типа пошло не так !")
                    print("Преобразование типа пошло не так !\n")
                    continue
                break
            input("Нажмите Enter для продолжения!")
            continue
        if switch == "2":
            while True:
                try:
                    counter = 0
                    for i in this_company.workerList:
                        print("№{}\n{}".format(counter, i))
                        counter += 1
                    num = int(input("\nВведите номер работника:"))
                    if len(this_company.workerList) > num:
                        this_company.workerList.remove(this_company.workerList[num])
                except ValueError:
                    log.exception("Неправильный ввод!")
                    print("Неправильный ввод!\n")
                    continue
                break
            input("Нажмите Enter для продолжения!")
            continue
        if switch == "3":
            input("Нажмите Enter для продолжения!")
            continue
        if switch == "4":
            for i in this_company.positionDict:
                print("{} -> {}".format(i, this_company.positionDict[i]))
            input("Нажмите Enter для продолжения!")
            continue
        if switch == "5":
            while True:
                try:
                    position = input("Введите название должности:")
                    num = int(input("Введите количество вакансий для данной должности:"))
                    this_company.positionDict[position] = num
                except ValueError:
                    log.exception("Неправильный ввод!")
                    print("Неправильный ввод:")
                    continue
                break
            input("Нажмите Enter для продолжения!")
            continue
        if switch == "6":
            while True:
                position = input("Введите название должности:")
                if position in this_company.positionDict:
                    del this_company.positionDict[position]
                else:
                    print("Вакансия не обноружена ! (Возможно вам стоит уволить сотрудника!)")
                break
            input("Нажмите Enter для продолжения!")
            continue
        if switch == "7":
            name = input("Введите имя (или часть имени):")
            flag = True
            for i in this_company.workerList:
                if name in i.name:
                    print(i)
                    flag = False
            if flag:
                print("Ничего не найдено!")
            input("Нажмите Enter для продолжения!")
            continue
        if switch == "8":
            for i in this_company.workerList:
                print(i)
            input("Нажмите Enter для продолжения!")
            continue
        if switch == "9":
            this_company.workerList.sort(key=lambda this_worker: this_worker.name)
            input("Нажмите Enter для продолжения!")
            continue
        if switch == "10":
            for i in this_company.workerList:
                if i.birthday.month == datetime.date.today().month:
                    print(i)
            input("Нажмите Enter для продолжения!")
            continue
        if switch == "11":
            return
        else:
            print("Неправильный ввод!")
            input("Нажмите Enter для продолжения!")
            continue


def transport_control(this_company: company.Company) -> None:
    pass


def order_control(this_company: company.Company) -> None:
    pass


def view_info(this_company: company.Company) -> None:
    while True:
        switch = input("(1)Отобразить список работников\n(2)Отобразить список вакансий\n"
                       "(3)Отобразить список транспорта\n(4)Отобразить список заказов\n(5)Назад\n")
        if switch == "1":
            for i in this_company.workerList:
                print(i)
            continue
        if switch == "2":
            for i in this_company.positionDict:
                print(i)
            continue
        if switch == "3":
            for i in this_company.transportList:
                print(i)
            continue
        if switch == "4":
            for i in this_company.orderList:
                print(i)
            continue
        if switch == "5":
            return


if __name__ == "__main__":
    main()
