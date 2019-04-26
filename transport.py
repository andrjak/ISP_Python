import webbrowser


class TransportInfo:
    __doc__ = "Описание модели транспорта, производителя, год выпуска."

    def __init__(self, name, producer, year):
        self.name = name  # Название модели
        self.producer = producer  # Фирма производитель
        self.year = year  # Год выпуска

    def get_producer_info(self):  # Перейти на сайт фирмы
        webbrowser.open_new("https://www.{company}.by".format(company=self.producer))

    def get_model_info(self):  # Запрос по модели транспорта
        webbrowser.open_new("https://google.com/search?q={company}+{model}".format(
            company=self.producer, model=self.name))

    def get_price_info(self):  # Запрос о цене транспортного средства
        webbrowser.open_new("Стоимость {company} {model}".format(company=self.producer, model=self.name))


class Transport:
    __doc__ = "Основной класс описывающий транспортное средство"

    def __init__(self, info: TransportInfo, status="Готов к работе", warranty_service=False,
                 repairs=False, insurance=False, maintenance_cost=None, fuel_consumption=None, crew=None):
        self.info = info  # Информация о трансрорте
        self.warranty_service = warranty_service  # Гарантийное обслуживание
        self.repairs = repairs  # Есть ли повреждения (необходим ли ремонт)(стоимость ремонта)
        self.insurance = insurance  # Есть ли страховка (и какая)
        self.maintenance_cost = maintenance_cost  # Стоимость технического обслуживания(неучитывая топливо)
        self.fuel_consumption = fuel_consumption  # Средний расход топлива на 100 км
        self.crew = crew  # Экипаж
        self.status = status  # Статус (занят на рейсе, в ремонте, свободен)

    def __str__(self):
        return "Производитель: {} Модель: {} Статус: {}".format(self.info.producer, self.info.name, self.status)


class Truck(Transport):  # Грузовой автомобиль
    __doc__ = "Класс грузового автомобиля"

    def __init__(self, info, carrying, status="Готов к работе", warranty_service=False,
                 repairs=False, insurance=False, maintenance_cost=None, fuel_consumption=None, crew=None):
        Transport.__init__(self, info, status, warranty_service,
                           repairs, insurance, maintenance_cost, fuel_consumption, crew)
        self.carrying = carrying  # Грузоподёмность (не включая пасажиров и экипаж) // для грузового


class Car(Transport):  # Легковой автомобиль (универсальный для небольших заказов)
    __doc__ = "Класс легкового автомобиля"

    def __init__(self, info, carrying, number_of_seats, status="Готов к работе", warranty_service=False,
                 repairs=False, insurance=False, maintenance_cost=None, fuel_consumption=None, crew=None):
        Transport.__init__(self, info, status, warranty_service,
                           repairs, insurance, maintenance_cost, fuel_consumption, crew)
        self.carrying = carrying  # Грузоподёмность
        self.number_of_seats = number_of_seats  # Количество пасажиров


class Bus(Transport):  # Автобус
    __doc__ = "Класс автобуса"

    def __init__(self, info, number_of_seats, status="Готов к работе", warranty_service=False,
                 repairs=False, insurance=False, maintenance_cost=None, fuel_consumption=None, crew=None):
        Transport.__init__(self, info, status, warranty_service,
                           repairs, insurance, maintenance_cost, fuel_consumption, crew)
        self.number_of_seats = number_of_seats  # Количество пасажиров


if __name__ == "__main__":
    x = Transport(TransportInfo("S8", "Audi", 2015))
    x.info.get_producer_info()
    x.info.get_model_info()
