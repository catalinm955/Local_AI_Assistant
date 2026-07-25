import logging

logger = logging.getLogger("Local_AI_Assistant")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

console_handler.setFormatter(console_formatter)

logger.addHandler(console_handler)