from Model import transport, worker
import datetime


class Order:
    __doc__ = "Описание заказов"

    def __init__(self, customer, order_transport: transport.Transport, workers: [worker.Worker],
                 start_date: datetime.date, end_date: datetime.date, route, payment):
        self.customer = customer  # Информация о заказчике
        self.order_transport = order_transport
        order_transport.status = "выполняет заказ"
        self.workers = workers
        self.start_date = start_date
        self.end_date = end_date
        self.payment = payment
        self.route = route

    def __str__(self):
        return "Заказчик: {} \nТранспорт:\n{}\nНачало: {} Конец: {}".format(
            self.customer, self.order_transport, self.start_date, self.end_date)

    def get_net_profit(self):
        worker_cost = 0
        for i in self.workers:
            worker_cost += i.get_cost(self.start_date, self.end_date)

        return self.payment - worker_cost - self.order_transport.maintenance_cost\
                            - self.route * self.order_transport.fuel_consumption

    def get_new_payment(self, const):  # Const - процет прибыли(%)
        worker_cost = 0
        for i in self.workers:
            worker_cost += i.get_cost(self.start_date, self.end_date)
        pay = worker_cost + self.order_transport.maintenance_cost + self.route * self.order_transport.fuel_consumption

        return pay + pay * const / 100


if __name__ == "__main__":
    x = Order("oao.db", transport.Transport(transport.TransportInfo("S8", "Audi", 2015)),
              worker.Worker("Валетко Андрей Николаевич", "Директор", datetime.date(2000, 4, 21), 1000,
                            datetime.date(2, 1, 1), 8, datetime.date(2018, 2, 1)),
              datetime.date(2018, 8, 10), datetime.date(2018, 9, 10), 100, 100)
    print(x)
