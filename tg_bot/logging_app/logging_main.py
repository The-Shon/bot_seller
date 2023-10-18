import logging
import logging.config

logging_bot = logging.basicConfig(level=logging.INFO, format='%(asctime)s - [%(levelname)s] - %(name)s - '
                        '(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s')
    
CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,


    "formatters": {
        "simple": {
            "format": "%(asctime)s - [%(levelname)s] - %(name)s - "
                        "%(funcName)s[%(filename)s].(%(lineno)d) - %(message)s"
        }
    },


    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "stderr": {
            "class": "logging.StreamHandler",
            "level": "ERROR",
            "formatter": "simple",
            "stream": "ext://sys.stderr"
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "simple",
            "filename": "app.log",
            "mode": "w"
        }
    },

    "loggers": {
        "root": {
            "level": "DEBUG",
            "handlers": [
                "stderr",
                "stdout",
                "file"
            ],
            "propagate": True
        }, 
    }
}