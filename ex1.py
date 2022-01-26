import imp
from flask import Flask, request
import redis 
from rq import Queue
import time
"""
a simple app to demonstrate the use of message brokers and queues in flask
"""
app = Flask(__name__)

# connect to redis instance
redis_instance = redis.Redis()

# create queue and connect to redis
# queue we can push our tasks to. 
queue = Queue(connection=redis_instance)

#function to handle tasks
def background_tasks(name):
    #simulate a delay
    delay = 2
    print("Task running ")
    print(f"simulating {delay}second delay")
    time.sleep(delay)
    print("task complete")
    return len(name)

@app.route('/task')
def add_task():
    if request.args.get("name"):
        # add job to queue
        job = queue.enqueue(background_tasks,request.args.get("name"))
        queue_len = len(queue)
        return f"task added to queue at {job.id}. {job.enqueued_at} . {queue_len} tasks in the queue"
    return "No argument to route"



