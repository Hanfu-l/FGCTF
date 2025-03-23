import redis
from django.conf import settings
import json

class RedisClass:

    def __init__(self, pool_name='RedisClass'):
        # Redis 客户端连接
        self.redis_client = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        self.pool_name = pool_name

            
    def Create_Lock(self,name):
        return self.redis_client.set(name,"LOCKED",ex=10,nx=True)

    def Delete_Lock(self,name):
        if self.redis_client.get(name) == "LOCKED":  # 确保锁存在
            return self.redis_client.delete(name)  # 删除锁
        return False  # 锁不存在或已经被其他进程释放


    #存入新问题
    def Put_Questions(self,key,question,answer):
            data=json.dumps({"question":question,"answer":answer})
            self.redis_client.lpush(key,data)
            self.redis_client.ltrim(key,0,2)
        

    #获取问题
    def Get_QuestionsData(self,key):
        questiondata=self.redis_client.lrange(key,0,-1)
        parsed_data = [json.loads(item) for item in questiondata]
        return parsed_data



class LeaderBoard:
    def __init__(self):
        # Redis 客户端连接
        self.redis_client = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

    #添加用户
    def add_user(self,username,score):
        self.redis_client.zadd('leaderboard',{username:score})

    #更新用户信息
    def update_user_score(self,username,score):
        self.redis_client.zadd('leaderboard',{username:score},xx=True)
    

    #获取前50名排行榜信息
    def get_rank(self):
        return self.redis_client.zrevrange('leaderboard',0,50,withscores=True)


    #获取当前用户排名
    def get_user_leaderboard(self,username):

        return self.redis_client.zrevrank('leaderboard',username)

    def if_leaderboard(self):
        return self.redis_client.exists('leaderboard')