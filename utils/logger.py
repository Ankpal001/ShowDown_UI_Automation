import logging
import os


class Logger:

    @staticmethod
    def get_logger(name):
        os.makedirs("logs", exist_ok=True)

        logger = logging.getLogger(name)

        if not logger.handlers:
            logger.setLevel(logging.INFO)

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
            )

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            file_handler = logging.FileHandler(
                "logs/automation.log",
                encoding="utf-8"
            )
            file_handler.setFormatter(formatter)

            logger.addHandler(console_handler)
            logger.addHandler(file_handler)

        return logger