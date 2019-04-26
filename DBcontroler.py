import pymongo

client = pymongo.MongoClient()
db = client["mainDataBase"]


def worker_list_get():
    collection = db["workerDB"]


def transport_list_get():
    collection = db["transportDB"]


def order_list_get():
    collection = db["orderDB"]


def partner_list_get():
    collection = db["partnerDB"]


def position_dict_get():
    collection = db["positionDB"]


def worker_list_set():
    pass


def transport_list_set():
    pass


def order_list_set():
    pass


def partner_list_set():
    pass


def position_dict_set():
    pass


if __name__ == "__main__":
    pass
