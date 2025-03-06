import redis
from django.conf import settings


class PortPool:

    def __init__(self, pool_name='port_pool'):
        # Redis 客户端连接
        self.redis_client = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)
        self.pool_name = pool_name

    def initialize_pool(self):
        """
        初始化端口池，填充可用端口集合
        """
        minport=settings.PRESET_PORTS[0]
        maxport=settings.PRESET_PORTS[1]
        for i in range(minport,maxport):
            self.redis_client.sadd(self.pool_name, i)
            
    def get_available_port(self):
        """
        获取一个可用端口，如果池中没有可用端口，返回 None
        """
        port = self.redis_client.spop(self.pool_name)
        return port if port else None

    def release_port(self, port):
        """
        将使用完的端口归还到 Redis Set 中
        """
        self.redis_client.sadd(self.pool_name, port)

    def get_all_ports(self):
        """
        获取池中的所有端口
        """
        return self.redis_client.smembers(self.pool_name)

    def clear_pool(self):
        """
        清空池中所有端口
        """
        self.redis_client.delete(self.pool_name)