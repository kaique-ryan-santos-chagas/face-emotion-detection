import schedule
import time

from src.Job import Job 

job = Job()

schedule.every().day.at('17:25').do(job.startDetection)

while True:

    schedule.run_pending()
    time.sleep(1)