import logging

logging.basicConfig(filename="log_file.log", format="%(asctime)s %(message)s"
                    ,filemode="w")

logger = logging.getLogger()
