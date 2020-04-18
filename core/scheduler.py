from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess

sched = BlockingScheduler()

@sched.scheduled_job('interval', hours=1)
def timed_job():
    command = "python manage.py repo | grep True > /dev/null && python manage.py seed"
    subprocess.Popen([command], shell=True)


sched.start()
