from datetime import datetime, timedelta
from time import sleep


def sleeper(seconds, reason=''):
    now = datetime.now() + timedelta(seconds=seconds)
    formatted_time = now.strftime("%H:%M:%S")
    if reason == '':
        print("Sleeping until {}".format(formatted_time))
    else:
        print("{}\n"
              "Sleeping until {}".format(reason, formatted_time))
    sleep(seconds)
    print("Resuming...")

