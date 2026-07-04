from extensions import redis_client

redis_client.delete("test", "hello")
value=redis_client.get("test")
print(value)