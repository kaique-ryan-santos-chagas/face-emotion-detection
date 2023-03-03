import schedule
import time

from src.Job import Job

job = Job()

schedule.every().day().at('17:55').do(job.start)

while True:

    schedule.run_pending()
    time.sleep(1)