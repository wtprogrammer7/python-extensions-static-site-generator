from ssg import hooks
import time

start_time = None
total_written = 0

@hooks.register("start_build")
def start_build():
    global start_time
    x = time.localtime()
