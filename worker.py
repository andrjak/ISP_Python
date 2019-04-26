import datetime


class Worker:
    __doc__ = "Класс описывающий работника предприятия"

    def __init__(self, name, position, birthday,
                 salary, experience: datetime.date = datetime.date(1, 1, 1),
                 duration=8, date=datetime.date.today()):
        self.name = name  # Фамилия Имя Отчество
        self.position = position  # Должность
        self.date = date  # Первый рабочий день
        self.birthday = birthday  # День рождения
        self.duration = duration  # Продолжительность рабочего дня
        self.salary = salary  # Зарплата за час
        self.experience = experience  # Стаж
        self.days_over_normal = 0  # Количество часов отработаных вне рабочее время
        self.previous_payday = date  # Предыдущая зарплата расчитана до этого дня

    def __str__(self):
        return "{}  ->  {}\nЗарплата в час: {}$  Стаж: {}\nДень рождения: {}".format(
            self.name, self.position, self.salary, self.experience, self.birthday)

    def get_experience_bonus(self) -> float:
        return self.experience.year * 0.02 * self.salary

    def get_salary(self, flag=False):  # flag - переместить указатель зарплаты на текущий день
        time = (datetime.date.today() - self.previous_payday).days
        time = int(time)
        result = self.salary * self.duration * time + \
            self.get_experience_bonus() * time + 2 * self.days_over_normal * self.salary

        if flag:
            self.previous_payday = datetime.date.today()
            self.days_over_normal = 0
        return result

    def get_cost(self, start_day: datetime.date, end_day: datetime.date):
        time = int((end_day - start_day).days)
        return time * self.salary * self.duration + self.get_experience_bonus() * time

    def get_experience_this_work(self):
        return datetime.date.today() - self.date


if __name__ == "__main__":
    x = Worker("Валетко Андрей Николаевич", "Директор", datetime.date(2000, 4, 21),
               1000, datetime.date(2, 1, 1), 8, datetime.date(2018, 2, 1))
    print(x)
