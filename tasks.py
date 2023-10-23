from celery import Celery

app = Celery('tasks', backend='rpc://', broker='pyamqp://')

@app.task
def add(x, y):
    return x+y

@app.task
def divide(a, b):
    return a/b