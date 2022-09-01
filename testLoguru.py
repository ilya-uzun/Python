
from loguru import logger

new_level = logger.level("SNAKY", no=38, color="<yellow>", icon="🐍")
logger.add("file.log", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")
logger.log("SNAKY", "Here we go!")

# logger.add("debug.json", format="{time} {level} {message}",
#            level="DEBUG", serialize=True)
#
# def divide(a, b):
#     return a / b
#
# @logger.catch
# def main():
#     divide(1, 0)
#
#
# main()