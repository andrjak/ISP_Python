import pymongo
import datetime
from Model import company
from Model.worker import Worker
from Model.transport import Transport, TransportInfo

client = pymongo.MongoClient()
db = client["mainDataBase"]


def get_data(this_company):
    workers = db["worker_list"].find()
    worker_list = list()
    for i in workers:
        birthday = datetime.datetime.strptime(i["birthday"], "%d.%m.%Y")
        date = datetime.datetime.strptime(i["date"], "%d.%m.%Y")
        worker_list.append(Worker(i["name"], i["position"], birthday, i["salary"],
                                  i["experience"], i["duration"], date))

    transports = db["transport_list"].find()
    transport_list = list()
    for i in transports:
        transport_list.append(Transport(TransportInfo(i["name"], i["producer"], i["year"]),
                                        i["insurance"], i["warranty_service"]))

    this_company.start_init(transport_list, worker_list, [1, 2, 3], [1, 2, 3], {"Программист": 2})


def set_data(this_company):
    workers = db["worker_list"]
    workers.remove({})
    for i in this_company.workerList:
        workers.save({"name": i.name, "position": i.position, "birthday": i.birthday.strftime("%d.%m.%Y"),
                      "salary": i.salary, "experience": i.experience,
                      "duration": i.duration, "date": i.date.strftime("%d.%m.%Y")})
    transports = db["transport_list"]
    transports.remove({})
    for i in this_company.transportList:
        transports.save({"name": i.info.name, "producer": i.info.producer, "year": i.info.year,
                         "insurance": i.insurance, "warranty_service": i.warranty_service})


def main():
    transport_collection = db["transport_list"]
    tr = Transport(TransportInfo("S8", "Audi", 2015))
    transport_collection.save({"name": tr.info.name, "producer": tr.info.producer, "year": tr.info.year,
                               "insurance": tr.insurance, "warranty_service": tr.warranty_service})


if __name__ == "__main__":
    # main()
    # set_data(company.Company())
    get_data(company.Company())
