import company
from Controller import viewController
import datetime
import logging
from worker import Worker

logging.basicConfig(filename="log.log", level=logging.INFO, format=
                    "%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s")
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning")
# logging.error("This is an error message")
# logging.critical("FATAL!!!")

log = logging.getLogger("mainLogger")


def main() -> None:
    this_company = company.Company()
    workers = [Worker("Валетко Андрей Николаевич", "Директор", datetime.date(2000, 4, 21),
                  1000, 2, 8, datetime.date(2018, 2, 1)), Worker("Горбачёв Дмитрий", "Зам Директора", datetime.date(2000, 8, 4),
                   900, 2, 8, datetime.date(2018, 2, 1)), Worker("Матюшонак Александр", "Зам Директора", datetime.date(2000, 1, 19),
                   950, 2, 8, datetime.date(2018, 2, 1))]

    this_company.start_init([1, 2, 3], workers, [1, 2, 3], [1, 2, 3], {"Программист": 2})
    viewController.main(this_company)


if __name__ == "__main__":
    main()
