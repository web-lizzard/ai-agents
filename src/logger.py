import sys

from loguru import logger

logger.remove()

def custom_format(record):
    level_color = {
        "DEBUG": "<light-red>",
        "INFO": "<cyan>",
        "SUCCESS": "<green>",
        "ERROR": "<red>"
    }
    color = level_color.get(record["level"].name, "<white>")
    return f"{color}{record['level'].icon}  [{record['level'].name}] [{record['time']:YYYY-MM-DD HH:mm:ss}] [{record['file'].name}] {record['message']}\n</>"

logger.add(sys.stderr, format=custom_format, colorize=True)

