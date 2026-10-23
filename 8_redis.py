from redis import Redis
import uuid

redis = Redis(host='localhost', port=6379, db=0)
key = 1
def set_key(key):

    token = str(uuid.uuid4())
    redis.set(key, token)

while True:
    inp=input('y/n:')
    if inp == 'y':
        set_key(key)
        key += 1

    elif inp == 'n':
        break
    else:
        print('Invalid input')