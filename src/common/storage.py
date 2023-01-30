from .configuration import configuration
from redis import Redis

storage = Redis(host=configuration["RedisHost"],
                port=configuration["RedisPort"],
                password=configuration["RedisPassword"])