import logging
logging.basicConfig(
    level=logging.DEBUG,
    filename="logs.log",
    filemode='a',
    format="%(levelname)s:%(asctime)s - %(message)s"
    )


# logging.debug("debug2")
logging.info("Всім")
# logging.warning("warning2")
# logging.error("error2")
# logging.critical("critical2")

# try:
#     print(10/0)
# except Exception:
#     logging.exception("Exception")
