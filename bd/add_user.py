
import redis
r = redis.Redis(host="localhost", port=6379)

def reg_check_user(user_id, user_name):
    if r.exists(f"{user_id}"):
        print("Exists")
    else:
        r.set(f"{user_id}", f"{user_name},{user_id}")

