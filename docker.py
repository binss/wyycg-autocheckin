import datetime
import os
import signal
import time
import locale
import gettext

from crontab import CronTab

time_format = "%Y-%m-%d %H:%M:%S"

def stop_me(_signo, _stack):
    print("Docker container has stoped....")
    exit(-1)

def main():
    signal.signal(signal.SIGINT, stop_me)

    print("Running genshinhelper with docker")
    env = os.environ
    cron_signin = env["CRON_SIGNIN"]
    cron = CronTab(cron_signin, loop=True, random_seconds=True)

    def next_run_time():
        nt = datetime.datetime.now().strftime(time_format)
        delayt = cron.next(default_utc=False)
        nextrun = datetime.datetime.now() + datetime.timedelta(seconds=delayt)
        nextruntime = nextrun.strftime(time_format)
        print("Current running datetime: {nt}".format(nt=nt))
        print("Next run datetime: {nextruntime}".format(nextruntime=nextruntime))

    def sign():
        print("Starting signing")
        os.system("python3 /app/main.py")

    sign()
    next_run_time()
    while True:
        ct = cron.next(default_utc=False)
        time.sleep(ct)
        sign()
        next_run_time()


if __name__ == '__main__':
    main()

