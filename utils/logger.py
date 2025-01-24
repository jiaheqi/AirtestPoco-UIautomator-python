from datetime import datetime


def log(message):
    time = datetime.now()
    print(f"{time} AutoUI - {message}")
