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

    def __init__(self, info: TransportInfo, warranty_service=False, insurance=False):
        self.info = info  # Информация о трансрорте
        self.warranty_service = warranty_service  # Гарантийное обслуживание
        self.insurance = insurance  # Есть ли страховка

    def __str__(self):
        warranty_service = "Гарантия истекла"
        insurance = "Не застраховано"
        if self.warranty_service:
            warranty_service = "На гарантии"
        if self.insurance:
            insurance = "Застраховано"
        return "Производитель: {} -> Модель: {} \n Гарантийное обслуживание: {}\n Страховка: {}".format(
            self.info.producer, self.info.name, warranty_service, insurance)


class Truck(Transport):  # Грузовой автомобиль
    __doc__ = "Класс грузового автомобиля"

    def __init__(self, info, carrying, warranty_service=False, insurance=False):
        Transport.__init__(self, info, warranty_service, insurance)
        self.carrying = carrying  # Грузоподёмность (не включая пасажиров и экипаж) // для грузового


class Car(Transport):  # Легковой автомобиль (универсальный для небольших заказов)
    __doc__ = "Класс легкового автомобиля"

    def __init__(self, info, carrying, number_of_seats, warranty_service=False, insurance=False):
        Transport.__init__(self, info, warranty_service, insurance)
        self.carrying = carrying  # Грузоподёмность
        self.number_of_seats = number_of_seats  # Количество пасажиров


class Bus(Transport):  # Автобус
    __doc__ = "Класс автобуса"

    def __init__(self, info, number_of_seats, warranty_service=False, insurance=False):
        Transport.__init__(self, info, warranty_service, insurance)
        self.number_of_seats = number_of_seats  # Количество пасажиров


if __name__ == "__main__":
    # x = Transport(TransportInfo("S8", "Audi", 2015))
    # x.info.get_producer_info()
    # x.info.get_model_info()
    pass
