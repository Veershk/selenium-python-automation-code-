import logging


class Logclass:
    def getthelogs(self):
        logger = logging.getLogger()
        filehandler = logging.FileHandler("..\\Logs\\logfile.log", mode="w")
        formatter = logging.Formatter("%(asctime)s %(levelname)s %(module)s %(functionName)s %(message)s",
                                      datefmt="%d,%m,%Y %I:%H:%M %S")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger
