import logging


class LogGen:
    @staticmethod
    def logGen():
        logger = logging.getLogger()
        filehandler = logging.FileHandler("Logs/automation.log", "w")
        formatter = logging.Formatter('%(asctime)s: %(levelname)s:%(module)s: %(message)s',
                                      datefmt='%d/%m/%Y %I:%M:%S %p')
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger


