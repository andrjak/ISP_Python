import company
import transport
import viewController
import worker
import order
import datetime
import logging

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
    this_company.start_init([1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3], {"Программист": 2})
    viewController.main(this_company)


if __name__ == "__main__":
    main()
