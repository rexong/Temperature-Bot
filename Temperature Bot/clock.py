from apscheduler.schedulers.blocking import BlockingScheduler
from addtemp import morning, afternoon

sched = BlockingScheduler()

# do at 7am
sched.add_job(morning, 'cron', day_of_week='mon-sun',
              hour=8, minute=30, jitter=1500)

# do at 4pm
sched.add_job(afternoon, 'cron', day_of_week='mon-sun',
              hour=20, minute=30, jitter=1500)

sched.start()
