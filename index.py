import schedule
import time

from src.Job import Job 

job = Job()

schedule.every().day.at('16:00').do(job.startCamera)

while True:

    schedule.run_pending()
    time.sleep(1)