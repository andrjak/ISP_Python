import pymongo
import datetime
from Model import company
from Model.worker import Worker

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
    this_company.start_init([1, 2, 3], worker_list, [1, 2, 3], [1, 2, 3], {"Программист": 2})


def set_data(this_company):
    workers = db["worker_list"]
    workers.remove({})
    for i in this_company.workerList:
        workers.save({"name": i.name, "position": i.position, "birthday": i.birthday.strftime("%d.%m.%Y"),
                      "salary": i.salary, "experience": i.experience,
                      "duration": i.duration, "date": i.date.strftime("%d.%m.%Y")})


def main():
    this_company = company.Company()
    workers = [Worker("Валетко Андрей Николаевич", "Директор", datetime.date(2000, 4, 21),
                      1000, 2, 8, datetime.date(2018, 2, 1)),
               Worker("Горбачёв Дмитрий", "Зам Директора", datetime.date(2000, 8, 4),
                      900, 2, 8, datetime.date(2018, 2, 1)),
               Worker("Матюшонак Александр", "Зам Директора", datetime.date(2000, 1, 19),
                      950, 2, 8, datetime.date(2018, 2, 1))]

    this_company.start_init([1, 2, 3], workers, [1, 2, 3], [1, 2, 3], {"Программист": 2})

    worker_collection = db["worker_list"]
    worker_collection.save({"name": workers[0].name, "position": workers[0].position, "birthday": "21.04.2000",
                            "salary": workers[0].salary, "experience": workers[0].experience,
                            "duration": workers[0].duration, "date": "01.02.2018"})
    worker_collection.save({"name": workers[1].name, "position": workers[1].position, "birthday": "04.08.2000",
                            "salary": workers[1].salary, "experience": workers[1].experience,
                            "duration": workers[1].duration, "date": "01.02.2018"})
    worker_collection.save({"name": workers[2].name, "position": workers[2].position, "birthday": "19.01.2000",
                            "salary": workers[2].salary, "experience": workers[2].experience,
                            "duration": workers[2].duration, "date": "01.02.2018"})


if __name__ == "__main__":
    # main()
    # set_data(company.Company())
    get_data(company.Company())
