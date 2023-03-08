import schedule
import time

from src.Job import Job 

job = Job()

schedule.every().day.at('15:35').do(job.startCamera)

while True:

    schedule.run_pending()
    time.sleep(1)