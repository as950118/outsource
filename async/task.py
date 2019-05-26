from celery import Celery
app = Celery('tasks', broker='amqp://guest:guest@localhost:6379//') # 브로커 설정
@app.task
def add(x,y):
    return x+y