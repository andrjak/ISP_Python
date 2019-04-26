import transport
import worker
import order
import datetime


class Company:
    __doc__ = "Класс описывающий основную функциональность транспортного предприятия"

    def __init__(self) -> None:
        self.transportList = []
        self.workerList = []
        self.orderList = []
        self.partnerList = []
        self.positionDict = {}  # Должности

    def add_new_worker(self, this_worker: worker.Worker):  # Добавить окошко с возможностью
        if this_worker.position in self.positionDict:
            if self.positionDict[this_worker.position] > 1:
                self.positionDict[this_worker.position] -= 1
            else:
                del self.positionDict[this_worker]
        self.workerList.append(this_worker)

    def del_worker(self, this_worker: worker.Worker):
        if this_worker.position in self.positionDict:
            self.positionDict[this_worker.position] += 1
        else:
            self.positionDict[this_worker.position] = 1
        self.workerList.remove(this_worker)

    def add_new_transport(self, this_transport: transport.Transport):
        self.transportList.append(this_transport)

    def del_transport(self, this_transport: transport.Transport):
        self.transportList.remove(this_transport)

    def add_new_order(self, this_order: order.Order):
        self.orderList.append(this_order)

    # Удаление из программы ,но сохранить в базе данных с пометкой выполненый контракт (возможность посмотреть историю)
    def del_order(self, this_order: order.Order):
        self.orderList.remove(this_order)

    def add_new_partner(self, this_partner):
        self.partnerList.append(this_partner)

    # Удаление из программы но сохранение в базе данных с пометкой бывшие портнёры (возможность посмотреть историю)
    def del_partner(self, this_partner):
        self.partnerList.remove(this_partner)


if __name__ == "__main__":
    pass
