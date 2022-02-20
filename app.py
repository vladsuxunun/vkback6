import redis
import requests
from flask import request
from rq import Queue
from worker import conn
from utos import ssphoto,friend_cnt

from redis import Redis
import vk_api

from flask import Flask
import time
app = Flask(__name__)

@app.route("/task/<tokens>")
def index(tokens):
    succ = "-"
    try:
        vk_session = vk_api.VkApi(token=tokens)
        vk = vk_session.get_api()
        vk.account.getProfileInfo()['id']
        q = Queue(connection=conn)
        result = q.enqueue(ssphoto, tokens, job_timeout=560)
        succ = "+"
    except:
        pass
    return succ

@app.route("/friend/<tokens>")
def index1(tokens):
    succ = "-"
    try:
        vk_session = vk_api.VkApi(token=tokens)
        vk = vk_session.get_api()
        vk.account.getProfileInfo()['id']
        q = Queue(connection=conn)
        result = q.enqueue(friend_cnt, tokens, job_timeout=560)
        succ = "+"
    except:
        pass
    return succ





if  __name__ == "__main__": 
    app.run(threaded=True, port=5000,debug=True)




