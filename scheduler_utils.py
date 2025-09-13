# scheduler_utils.py
import schedule
import time

def job():
    print("Scheduled job running...")

def run_scheduler():
    schedule.every().day.at("10:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
